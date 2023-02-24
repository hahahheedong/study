data = input()

temp = []
for c in data.split():
    temp.append(int(c))

a = temp[0]
b = temp[1]

if a > b:
    print(">")
elif a < b:
    print("<")
elif a == b:
    print("==")