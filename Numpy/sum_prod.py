import numpy as np

n, m = map(int, input().split())
a = np.array([input().split() for _ in range(n)], int)
print(np.product(np.sum(a, axis=0), axis=0))