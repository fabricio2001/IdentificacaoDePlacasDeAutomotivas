import re

p1 = "OJJ-3984"
p2 = "0JJ-3984"

x = p1

print(x[0:2].isalpha())
print(x[3] == '-')
print(x[4:7].isdigit())

if re.search("[A-Z/a-z/0-9]{3}-[0-9/A-Z/a-z]{4}", x):
    print(x)