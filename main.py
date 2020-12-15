from util import get_input
import importlib
import timeit


def main():
    DAY = int(input("Enter day to solve: "))
    content = get_input(DAY)
    module = importlib.import_module(f'src.{DAY}')
    start_time = timeit.default_timer()
    partOne = getattr(module, 'partOne')(content)
    p1_time = '{0:.5f}'.format(
        float(timeit.default_timer()) - float(start_time))
    partTwo = getattr(module, 'partTwo')(content)
    p2_time = '{0:.5f}'.format(float(timeit.default_timer()) - float(p1_time))
    print(
        f'Part One = {partOne} in {str(p1_time)} seconds\nPart Two = {partTwo} in {str(p2_time)} seconds')


if __name__ == "__main__":
    main()
