# Set Mutations

# Enter your code here. Read input from STDIN. Print output to STDOUT
m=int(input())
a = set(map(int, input().split()))
n= int(input())
for i in range(0,n):
    (cmd, newset) = (input().split()[0], set(map(int, input().split())))
    getattr(a,cmd)(newset)
print(sum(a))

