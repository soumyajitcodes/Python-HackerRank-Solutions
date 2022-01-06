import numpy

arr = numpy.array([int(i) for i in input().split()[:9]])
print(numpy.reshape(arr, (3, 3)))
