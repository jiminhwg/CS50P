import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    if s.startswith("<iframe"):
        if matches := re.search(r"https?://(?:www\.)?youtube\.(?:com)/embed/(\w+)", s): #https://docs.python.org/3/library/re.html#regular-expression-syntax
            return ("https://youtu.be/" + matches.group(1))

if __name__ == "__main__":
    main()