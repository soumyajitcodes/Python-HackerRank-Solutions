test_cases = int(input())
number_list = []
while test_cases:
    cmd_list = list(input().split())
    if cmd_list[0] == 'insert':
        number_list.insert(int(cmd_list[1]), int(cmd_list[2]))

    elif cmd_list[0] == 'print':
        print(number_list)

    elif cmd_list[0] == 'remove':
        number_list.remove(int(cmd_list[1]))

    elif cmd_list[0] == 'append':
        number_list.append(int(cmd_list[1]))

    elif cmd_list[0] == 'sort':
        number_list.sort()

    elif cmd_list[0] == 'pop':
        number_list.pop()

    elif cmd_list[0] == 'reverse':
        number_list.reverse()

    test_cases -= 1
