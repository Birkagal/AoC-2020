from util import get_input, start_clock, stop_clock, import_lib


def main():
    DAY = int(input("Enter day to solve: "))
    content = get_input(DAY)
    module = import_lib(DAY)
    start_time = start_clock()
    partOne = getattr(module, 'partOne')(content)
    p1_time = stop_clock(start_time)
    partTwo = getattr(module, 'partTwo')(content)
    p2_time = stop_clock(p1_time)
    print(
        f'Part One = {partOne} in {str(p1_time)} seconds\nPart Two = {partTwo} in {str(p2_time)} seconds')


if __name__ == "__main__":
    main()
