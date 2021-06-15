# Set .add()

n=int(raw_input())
s=set()
for _ in range(n):
    s.add(raw_input())
count=0
for i in s:
    count+=1
print(count)