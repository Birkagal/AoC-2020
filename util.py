import requests
import os
import timeit
import importlib
from dotenv import load_dotenv


load_dotenv()


def import_lib(name):
    return importlib.import_module(f'src.{name}')


def start_clock():
    return timeit.default_timer()


def stop_clock(start_time):
    return format_time(float(timeit.default_timer()) - float(start_time))


def format_time(time):
    return '{0:.5f}'.format(time)


def get_input_from_web(day):
    url = f'https://adventofcode.com/2020/day/{day}/input'
    headers_dict = {
        "cookie": "session=" + os.getenv("SESSION")}
    response = requests.get(url, headers=headers_dict)
    with open(f'./inputs/{day}.txt', 'w') as f:
        f.write(response.content.decode('utf-8'))


def get_input(day):
    file_path = f'./inputs/{day}.txt'
    if not os.path.isfile(file_path):
        get_input_from_web(day)
    return [x.rstrip() for x in open(file_path)]
