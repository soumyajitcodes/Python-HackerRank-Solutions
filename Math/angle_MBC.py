# -*- coding: utf-8 -*-
import math
AB = int(input())
BC = int(input())
res = str(int(round(math.atan2(AB, BC)/math.pi*180, 0)))
print(res,end='')
print(chr(176))