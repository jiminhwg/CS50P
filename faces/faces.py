word = input()

def main():
    convert()

def convert():
    if ":)" in word and ":(" in word:
        print(word.replace(":)", "🙂").replace(":(", "🙁"))
    elif ":(" in word:
        y = word.replace(":(", "🙁")
        print(y)
    elif ":)" in word:
        z = word.replace(":)", "🙂")
        print(z)

main()
