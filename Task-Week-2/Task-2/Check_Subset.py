# Check Subset

n=int(input())
for _ in range(0,n):
    a,seta = int(input()), set(map(int, input().split()))
    b,setb = int(input()), set(map(int, input().split()))
    if len(seta.difference(setb)) == 0:
        print('True')
    else:
        print('False')
    