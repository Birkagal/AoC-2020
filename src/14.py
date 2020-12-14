from functools import reduce
'''
Part One - Execute the initialization program. What is the sum of all values left in memory after it completes?
Part Two - Execute the initialization program using an emulator for a version 2 decoder chip. What is the sum of all values left in memory after it completes?
'''


def partOne(content):
    mem = dict()
    for line in content:
        if 'mask' in line:
            or_mask = int(line.split()[2].replace('X', '0'), 2)
            and_mask = int(line.split()[2].replace('X', '1'), 2)
        else:
            addr = line[4:].split(']')[0]
            mem[addr] = (int(line.split()[-1]) | or_mask) & and_mask
    return reduce(lambda a, b: a+(b if b != 0 else 0), list(mem.values()))


def partTwo(content):
    mem = dict()
    for line in content:
        if 'mask' in line:
            or_mask = int(line.split()[2].replace('X', '0'), 2)
            and_mask = int(line.split()[2].replace('X', '1'), 2)
            float_mask = line.split()[2].replace('1', '0')
        else:
            addresses = get_all_adresses(
                float_mask,  int(line[4:].split(']')[0]) | or_mask)
            value = int(line.split()[-1])
            for address in addresses:
                mem[int(address, 2)] = value
    return reduce(lambda a, b: a+(b if b != 0 else 0), list(mem.values()))


def get_all_adresses(float_mask, address):
    address = bin(address)[2:]
    address = '0' * (36 - len(address)) + address
    floating_index = []
    addresses = []
    for bit_index in range(36):
        if float_mask[bit_index] == 'X':
            floating_index.append(bit_index)
            address = address[:bit_index] + 'X' + address[(bit_index+1):]
    for option in range(2 ** address.count('X')):
        option = bin(option)[2:]
        option = '0' * (len(floating_index) - len(str(option))) + option
        new_address = list(address)
        for index, bit in enumerate(option):
            new_address[floating_index[index]] = bit
        addresses.append(''.join(new_address))
    return addresses
