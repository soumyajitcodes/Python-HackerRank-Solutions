from decimal import Decimal
from itertools import groupby, islice
from operator import itemgetter

a = []
for i in range(int(input())):
    x, y = (input(), Decimal(input()))
    a.append((y, x))
a.sort()
    for x in v:
        print(x[1])