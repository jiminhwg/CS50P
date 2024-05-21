def main():
    string = input("Fraction: ")
    percentage = convert(string)
    fuel = gauge(percentage)

    print(fuel)

def convert(fraction):
    while True:
        try:
            x,y = map(int, fraction.split('/'))

            if x > y:
                fraction = input("Fraction: ")
                a,b = map(int, fraction.split('/'))
                fraction = (int((a/b)*100))
            else:
                fraction = (int((x/y)*100))

            return fraction
        except (ValueError, ZeroDivisionError):
            raise

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return (str(percentage)+"%")

if __name__ == "__main__":
    main()
