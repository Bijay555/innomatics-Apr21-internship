#Find the Runner-Up Score!

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())

arr=sorted(arr)
a=arr[0]
b=arr[0]
for i in range(1,n):
    if(arr[i]==a):
        pass
    elif(arr[i]>a):
        a=arr[i]
        b=arr[i-1]

print(b)