# Set .symmetric_difference() Operation

n=input()
a = set(map(int, input().split()))
m=input()
b = set(map(int, input().split()))
print(len(a.symmetric_difference(b)))
