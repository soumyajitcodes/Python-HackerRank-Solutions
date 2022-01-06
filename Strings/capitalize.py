def solve(s):
    l = s.split()
    capitalized_list = []
    sum = ' '
    for i in l:
        capitalized_list.append(i.capitalize())
    return ' '.join(capitalized_list)

if __name__ == '__main__':

    s = input()
    result = solve(s)
    print(result)

