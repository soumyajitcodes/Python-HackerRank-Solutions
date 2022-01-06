def print_full_name(a, b):
    print(f"Hello {a} {b}! You just delved into python.")

if __name__ == '__main__':
    first_name = input()[:10]
    last_name = input()[:10]
    print_full_name(first_name, last_name)