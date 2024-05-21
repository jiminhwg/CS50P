word = input("camelCase: ")

List = []

for a in word:
    if a in "abcdefghijklmnopqrstuvwxyz":
        List.append(a)
    elif a in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        List.append("_")
        List.append(a)

print("snake_case:", end = " ")
for b in List:
    print(b.lower(), end = "")