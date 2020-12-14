from util import get_input
import importlib


def main():
    DAY = '14'
    content = get_input(DAY)
    module = importlib.import_module(f'src.{DAY}')
    partOne = getattr(module, 'partOne')
    partTwo = getattr(module, 'partTwo')
    print(f'Part One = {partOne(content)}\nPart Two = {partTwo(content)}')


if __name__ == "__main__":
    main()
