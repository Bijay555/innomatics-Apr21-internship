#Detect Floating Point Number

import re
for _ in range(0, int(input())):
    print(bool(re.match(r"^[-+]?\d*\.\d+$",input())))