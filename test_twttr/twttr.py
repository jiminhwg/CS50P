def main():
    word = input("Input: ")
    print("Output:", end = shorten(word))

def shorten(word):
    List = []

    for a in word:
        if a in "aeiouAEIOU":
            continue
        else:
            List.append(a)

    final_word = ""

    return final_word.join(List)


if __name__ == "__main__":
    main()
