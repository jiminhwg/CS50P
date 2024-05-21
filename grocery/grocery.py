grocery = []

while True:
    try:
        word = input()
        grocery.append(word)

        continue
    except (EOFError, KeyError):
        break
    else:
        continue

new_grocery = sorted(set(grocery))

for a in new_grocery:
    print(grocery.count(a), end = " ")
    print(a.upper())
