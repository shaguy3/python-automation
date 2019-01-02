def convert_d_b(decimal):
    binary = 0
    counter = 0
    if decimal == 0:
        return 0
    if decimal == 1:
        return 1
    while decimal > 1:
        if not decimal % 2 == 0:
            binary += 10 ** counter
        counter += 1
        decimal //= 2
    binary += 10 ** counter
    return binary


def convert_b_d(binary):
    if binary == 0:
        return 0
    if binary == 1:
        return 1
    decimal = 0
    binary_str = str(binary)
    while not binary_str == '':
        if binary_str is None:
            return decimal
        elif binary_str[0] == '0':
            decimal = decimal * 2
        elif binary_str[0] == '1':
            decimal = (decimal * 2) + 1
        binary_str = binary_str[1:]
    return decimal
