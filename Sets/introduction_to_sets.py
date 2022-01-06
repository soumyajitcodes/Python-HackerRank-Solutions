def average(array):
    set_array = set(array)
    avg = float(sum(set_array)/len(set_array))
    return avg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)