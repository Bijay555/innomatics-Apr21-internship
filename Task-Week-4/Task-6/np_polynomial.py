import numpy
a=list(map(float,raw_input().split()))
b=int(raw_input())
print(numpy.polyval(a,b))
