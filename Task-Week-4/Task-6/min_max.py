import numpy as np
n,m=map(int, input().split())
a = np.array([input().strip().split() for _ in range(n)], int)
a = np.min(a, axis=1)
print(np.max(a))