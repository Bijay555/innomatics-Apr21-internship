# Check Strict Superset

mainset=set(map(int, input().split()))
_ = int(input())
seta = set(map(int, input().split()))
setb = set(map(int, input().split()))
var1=False
if(len(seta.difference(mainset)) == 0 & len(seta)!=len(mainset)):
    if(len(setb.difference(mainset)) == 0 & len(setb)!=len(mainset)):
        var1=True
print(var1)
