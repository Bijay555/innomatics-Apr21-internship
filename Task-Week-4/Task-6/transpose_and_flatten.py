import numpy as np

m,n =map(int, input().split())
array = np.array([input().strip().split() for _ in range(n)], int)
print(np.transpose(array))
print(array.flatten())