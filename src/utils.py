import os
import timeit
import requests
from termcolor import colored


def get_input_from_web(day: str, year: str = 2022) -> str:
    print(colored('Input file not found, downloading from web...', 'magenta'))
    headers = {
        "cookie": "session=" + os.environ.get('SESSION')}
    response = requests.get(
        f'https://adventofcode.com/{year}/day/{day}/input',
        headers=headers
    )
    data = response.content.decode('utf-8')
    return data


def get_input(day: str, year: str = 2022):
    input_path = f'./inputs/{year}'
    if not os.path.exists(input_path):
        os.makedirs(input_path)
    if not os.path.isfile(f'{input_path}/{day}.txt'):
        input = get_input_from_web(day, year)
        with open(f'{input_path}/{day}.txt', 'w') as f:
            f.write(input)
    else:
        with open(f'{input_path}/{day}.txt') as f:
            input = f.read()
    return [line.rstrip() for line in open(f'{input_path}/{day}.txt')]


def stop_clock(start_time):
    return '{0:.5f}'.format(current_time() - float(start_time))


def current_time():
    return timeit.default_timer()


def get_day_year():
    year = os.environ.get('YEAR')
    if year is None:
        year = input(colored('Enter AOC year (Empty for 2022): ', 'yellow'))
        if year == '':
            year = '2022'
    day = input(colored('Enter day to solve: ', 'yellow'))
    return day, year
