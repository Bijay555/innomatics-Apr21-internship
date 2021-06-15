#Set .discard(), .remove() & .pop()

n = int(input())
s = set(map(int, input().split()))
m = int(input())
for  i in range(m):
    attr, *kw = input().split()
    if kw:
        getattr(s,attr)(*(map(int, *kw)))
    else:
        getattr(s,attr)()
print(sum(s))