import re

def main():
    print(count(input("Text: ")))


def count(s):
    count = 0
    s = s.lower()
    s = re.sub(r'[!\"#\＄%&\'\(\)\*\+,-\./:;<=>\?@\[\\\]\^_`{\|}~]','',s) #https://www.educative.io/answers/remove-all-the-punctuation-marks-from-a-sentence-using-regex
    s = s.split(" ")

    for a in s:
        if a == "um":
            count += 1
        else:
            continue
    return(count)

if __name__ == "__main__":
    main()