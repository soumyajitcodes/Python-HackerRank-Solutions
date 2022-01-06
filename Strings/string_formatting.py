def binary(number):
        return bin(number).replace('0b', ' ')

def octal(number):
    return oct(number).replace('0o', ' ')

def hexadecimal(number):
    return hex(number).replace('0x', ' ').upper()

def print_formatted(number):
    for i in range(1, number+1):
        res = [str(i), str(octal(i)), str(hexadecimal(i)), str(binary(i))]
        print("".join(res))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)