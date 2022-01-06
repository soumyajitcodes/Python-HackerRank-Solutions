n = int(input())
num_arr = set(map(int, input().split()))
N = int(input())
while N:
    cmd_list = list(input().split())
    if cmd_list[0] == 'pop':
        num_arr.pop()
    elif cmd_list[0] == 'remove':
        num_arr.remove(int(cmd_list[1]))
    elif cmd_list[0] == 'discard':
        num_arr.discard(int(cmd_list[1]))
    N -= 1

print(sum(num_arr))