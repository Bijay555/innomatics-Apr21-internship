# Enter your code here. Read input from STDIN. Print output to STDOUT
import math 
AB = int(input()) 
BC = int(input()) 
ans = int(round(math.degrees(math.atan2(AB,BC))))
degree=chr(176)
print(ans,degree,sep='')