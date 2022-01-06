from collections import deque

d = deque()
n = int(input())
while(n):
    cmd_list = input().split()
    if cmd_list[0] == 'append':
        d.append(int(cmd_list[1]))

    elif cmd_list[0] == 'appendleft':
        d.appendleft(int(cmd_list[1]))

    elif cmd_list[0] == 'pop':
        d.pop()

    elif cmd_list[0] == 'popleft':
        d.popleft()

    n -= 1

for i in d:
    print(i, end=' ')