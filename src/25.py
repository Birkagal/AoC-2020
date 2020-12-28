'''
Part One - What encryption key is the handshake trying to establish?
'''


def partOne(content):
    first_pkey = int(content[0])
    second_pkey = int(content[1])

    counter = 1
    value = 7
    while value != first_pkey and value != second_pkey:
        value = (value*7) % 20201227
        counter += 1

    enc_key = 0
    if value == first_pkey:
        enc_key = pow(second_pkey, counter, 20201227)
    else:
        enc_key = pow(first_pkey, counter, 20201227)
    return enc_key


def partTwo(content):
    pass
