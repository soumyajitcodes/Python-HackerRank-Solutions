import numpy as np

np.set_printoptions(sign=' ')
arr = [float(x) for x in input().split()]
arr = np.array(arr)
print(np.floor(arr))
print(np.ceil(arr))
print(np.rint(arr))