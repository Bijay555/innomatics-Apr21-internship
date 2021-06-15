# No Idea!

# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=map(int,raw_input().split())
x=raw_input().split(' ')
a=set(raw_input().split(' '))
b=set(raw_input().split(' '))
happiness=0
for i in x:
    if i in a:
        happiness +=1
    if i in b:
        happiness -=1
print(happiness)