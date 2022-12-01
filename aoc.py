import importlib
from termcolor import colored
from dotenv import load_dotenv
from pyfiglet import figlet_format

from src.utils import get_day_year, get_input, stop_clock, current_time


load_dotenv()


if __name__ == '__main__':
    print(colored(figlet_format('AdventOfCode', font='standard'), 'green'), end='')
    day, year = get_day_year()
    input = get_input(day, year)
    module = importlib.import_module(f'src.{year}.{day}')
    start_time = current_time()
    p1_result = module.part_one(input)
    p1_time = stop_clock(start_time)
    start_time = current_time()  # Restart clock
    p2_result = module.part_two(input)
    p2_time = stop_clock(start_time)

    # Show the result
    print(colored('RESULTS::', 'cyan'))
    print(
        colored(
            f'Part One = {p1_result} in {p1_time} seconds\nPart Two = {p2_result} in {p2_time} seconds',
            'blue'
        ))
