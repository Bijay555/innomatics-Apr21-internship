import numpy as np

n,m = map(int, input().split())
a = np.array([input().strip().split() for _ in range(n)],int)
b = np.array([input().strip().split() for _ in range(n)],int)
print(np.add(a,b))
print(np.subtract(a,b))
print(np.multiply(a,b))
print(a//b)
print(np.mod(a,b))
print(np.power(a,b))