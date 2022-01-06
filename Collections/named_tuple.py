from collections import namedtuple
N = int(input()); Student = namedtuple('Student', input().strip().split())
print(sum(float(Student(*input().split()).MARKS) for _ in range(N))/N)