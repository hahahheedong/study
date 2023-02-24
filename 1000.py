"""
data = input()

temp = []
for c in data.split():
    temp.append(int(c)) 

result = 0
for i in temp:
    result = result + i

print(result)
"""

data = input()

temp = []
for c in data.split():
    temp.append(int(c))

a = temp[0]
b = temp[1]

print(a+b)