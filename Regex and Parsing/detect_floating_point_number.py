import re

regex = r"[-+]?[0-9]*[.][0-9]+$"

T = int(input())
while T:
    try:
        test_str = input()
        # You can manually specify the number of replacements by changing the 4th argument
        result = re.match(regex, test_str)
        if result:
            print("True")
        else:
            print("False")
    except ValueError:
        print("False")
    T -= 1
