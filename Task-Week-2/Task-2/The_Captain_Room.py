# The_Captain_Room

# Enter your code here. Read input from STDIN. Print output to STDOUT
a,b = int(input()), list(map(int, input().split()))
m=set()
n=set()
for i in b:
    if i not in m:
        m.add(i)
    else:
        n.add(i)
print(m.difference(n).pop())
        
