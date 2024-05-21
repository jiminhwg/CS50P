amount_due = 50

while amount_due > 0:
    print("Amount Due:", end = " ")
    print(amount_due)
    money = int(input("Insert Coin: "))
    if money == 5 or money == 10 or money == 25:
        amount_due = amount_due - money
        continue
    else:
        continue

print("Change Owed:", end = " ")
print(-amount_due)

