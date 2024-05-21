print("Expression:", end = ' ')
x, y, z = map(str, input().split())

if y == "+":

elif y == "-":
    print(float(x)-float(z))
elif y == "*":
    print(float(x)*float(z))
else:
    print(float(x)/float(z))
