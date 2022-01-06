import numpy

N, M = map(int, input().split())
array = []
while N:
    element = [int(i) for i in input().split()]
    array.append(element)
    N -= 1

array = numpy.array(array)
print(numpy.transpose(array))
print(array.flatten())