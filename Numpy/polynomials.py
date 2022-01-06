import numpy as np

a = [float(i) for i in input().split()]
x = int(input())

print(np.polyval(a, x))
