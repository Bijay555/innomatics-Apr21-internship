import numpy
n=int(raw_input())
a=numpy.array([raw_input().split() for _ in range(n)],float)
#b=numpy.array(raw_input().split(),float)
print(numpy.linalg.det(a).round(2))