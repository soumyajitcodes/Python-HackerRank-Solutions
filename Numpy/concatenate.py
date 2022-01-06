import numpy as np

N, M, P = map(int, input().split())
matA = []
matB = []

while N:
    element = [int(i) for i in input().split()]
    matA.append(element)
    N -= 1

while M:
    element = [int(i) for i in input().split()]
    matB.append(element)
    M -= 1

matA = np.array(matA)
matB = np.array(matB)
print(np.concatenate((matA, matB), axis=0))