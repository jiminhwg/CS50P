from random import randint

def main():
    Level = get_level()
    start = generate_integer(Level)
    print("Score:", start)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level < 1:
                continue
            elif 1 <= level <= 3:
                return level
        except ValueError:
            continue


def Random(n):
    if n == 1:
        return randint(0, 9)
    else:
        range_start = (10**(n-1))
        range_end = (10**n)-1
        return randint(range_start, range_end)
        #code source: https://stackoverflow.com/questions/2673385/how-to-generate-a-random-number-with-a-specific-amount-of-digits

def generate_integer(level):
    score = 0

    for a in range(1,11):
        strike = 2
        b = Random(level)
        c = Random(level)
        while True:
            try:
                print(b,"+", c, "=", end = " ")
                answer = int(input())

                if b + c == answer:
                    score = score + 1
                    break
                else:
                    print("EEE")
                    if strike > 0:
                        strike = strike - 1
                        continue
                    elif strike == 0:
                        print(b,"+", c, "=", (b+c))
                        break
            except ValueError:
                continue

    return score


if __name__ == "__main__":
    main()