def main():
    question = convert(input("What time is it? "))

def convert(time):
    new = time.replace(":","")
    last_digits = float(new[-2:])/60
    hours = float(new[:-2]) + (last_digits)

    if 7 <= hours <= 8:
        print("breakfast time")
    elif 12 <= hours <= 13:
        print("lunch time")
    elif 18 <= hours <= 19:
        print("dinner time")

if __name__ == "__main__":
    main()