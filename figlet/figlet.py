from pyfiglet import Figlet
import random
import sys


figlet = Figlet()

try: #if there is input
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        try:
            f = Figlet(font = sys.argv[2])
            word = input("Input: ")
            print(f.renderText(word))
        except:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")

except IndexError: # if there is no input
    word = input("Input: ")
    f = Figlet(font = random.choice(figlet.getFonts()))
    print(f.renderText(word))


