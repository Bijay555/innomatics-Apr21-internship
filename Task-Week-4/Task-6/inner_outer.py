import numpy
a=numpy.array([raw_input().split()],int)
b=numpy.array([raw_input().split()],int)
print(numpy.inner(a,b)[0][0])
print(numpy.outer(a,b))
