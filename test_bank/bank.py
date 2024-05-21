def main():
    greeting = input("Greeting: ")
    print(f"${value(greeting)}")

def value(greeting):
    if "Hello" in greeting or "hello" in greeting:
        return 0
    elif greeting[0] == "H" or greeting[0] == "h":
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()




