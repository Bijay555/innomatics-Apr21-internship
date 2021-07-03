# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
n=int(input())

for i in range(0,n):
    print(re.sub(r"(?<= )(&&|\|\|)(?= )",lambda x: 'and' if x.group()=='&&' else 'or', input()))
    