word = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

if word.strip() == "42" or word.lower() == "forty-two" or word.lower() == "forty two":
    print("Yes")
else:
    print("No")