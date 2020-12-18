import requests
import os
import timeit
import importlib
from dotenv import load_dotenv


load_dotenv()


def get_day_output():
    DAY = int(input("Enter day to solve: "))
    content = get_input(DAY)
    module = importlib.import_module(f'src.{DAY}')
    start_time = timeit.default_timer()
    partOne = getattr(module, 'partOne')(content)
    p1_time = stop_clock(start_time)
    partTwo = getattr(module, 'partTwo')(content)
    p2_time = stop_clock(p1_time)
    return (partOne, p1_time, partTwo, p2_time)


def get_input(day):
    file_path = f'./inputs/{day}.txt'
    if not os.path.isfile(file_path):
        get_input_from_web(day)
    return [x.rstrip() for x in open(file_path)]


def get_input_from_web(day):
    url = f'https://adventofcode.com/2020/day/{day}/input'
    headers_dict = {
        "cookie": "session=" + os.getenv("SESSION")}
    response = requests.get(url, headers=headers_dict)
    with open(f'./inputs/{day}.txt', 'w') as f:
        f.write(response.content.decode('utf-8'))


def stop_clock(start_time):
    return '{0:.5f}'.format(timeit.default_timer() - float(start_time))
