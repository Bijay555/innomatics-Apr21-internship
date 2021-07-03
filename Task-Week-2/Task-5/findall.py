
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
a = re.findall(r'(?<=[b-df-hj-np-tv-zB-DF-HJ-NP-TV-Z])([AEIOU|aeiou]{2,})(?=[b-df-hj-np-tv-zB-DF-HJ-NP-TV-Z])', input())
if a==[]:
    print(-1)
else:
    for i in a:
        print(i)
 