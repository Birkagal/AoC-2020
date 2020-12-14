import requests
import os
from dotenv import load_dotenv

load_dotenv()


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
