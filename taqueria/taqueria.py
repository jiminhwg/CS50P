Menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

count = 0
while True:
    try:
        word = input("Item: ")
        if word.title() in Menu:
            print("Total: ", end = "$")
            count = count + Menu[word.title()]
            print(count, end ="0")
            print()
            continue
    except (EOFError, KeyError):
        break
    else:
        continue