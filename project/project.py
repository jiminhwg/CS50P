import os

def main():
    Load = loading_screen()
    name = input("What is your name? ")
    Intro = intro(name)
    os.system("clear")
    Start1 = question1(name)
    Start2 = question2(name)
    Start3 = question3(name)
    end = End(name)

def loading_screen():
    print("Welcome!")
    print("I am MathBot.")
    print("         __              ")
    print(" _(\    |..|             ")
    print("(__/\__ \--/ __          ") #robot ascii: https://www.asciiart.eu/electronics/robots
    print("   \___|----|  |   __    ")
    print("       \ }{ /\ )_ / _\   ")
    print("       /\__/\ \__O (__   ")
    print("      (--/\--)    \__/   ")
    print("      _)(  )(_           ")
    print("     `---''---`          ")
    return True

def intro(name):
    os.system("clear") #clear console
    print(f"Hello, {name}!")
    print("This short game consists of several questions to test your comprehension on elementary math word problems.")
    print(" * You will be given 3 multiple-choice questions to answer.")
    print(" * Input the respective letter (A, B, or C) of your answer.")
    print(" * You won't be graded and will be able to solve the problem as many times as you want.")
    print("Whenever you're ready, press Enter to begin!")
    start = input()
    return True

def question1(name): #math problems: intq
    os.system("clear")
    print("Question #1")
    print("At a store, you placed a soda, a chocolate bar, and a lollipop in your cart. These cost $1.25, $1.15, and $0.50 respectively.")
    print("However, you returned the chocolate bar, and added 2 more sodas into your cart.")
    print("How much money do you have to pay at the cash register?")
    print("A. $2.90")
    print("B. $4.25") #3 sodas, 1 lollipop
    print("C. $3.40")
    Answer = (answer_checker(1, input("Answer: "), name))
    return 1

def question2(name):
    os.system("clear")
    print("Question #2")
    print("Store A is selling 7 kilograms of bananas for $15.00.") #2.14 per kilo
    print("Store B is selling 3 kilograms of bananas for $7.00.") #2.3 per kilo
    print("Store C is selling 5 kilograms of bananas for $11.00.") #2.2 per kilo
    print("Which store has the better deal?")
    print("A. Store A")
    print("B. Store B")
    print("C. Store C")
    Answer = (answer_checker(2, input("Answer: "), name))
    return 2

def question3(name):
    os.system("clear")
    print("Question #3")
    print("The faces on a fair number die are labelled 1, 2, 3, 4, 5 and 6.")
    print("You roll the die 12 times.")
    print("How many times should you expect to roll a 1?")
    print("A. 1/6")
    print("B. 1/18")
    print("C. 1/12")
    Answer = (answer_checker(3, input("Answer: "), name))
    return 3

def answer_checker(question_num, answer, name):
    if question_num == 1:
        if answer == "B" or answer == "b":
            print(f"Congrats {name}! That's correct.")
            print("Press Enter to continue!")
            enter = input()
            os.system("clear")
        else:
            print(f"Oh no! That's incorrect.")
            answer = input("Would you like to try again? Y/N ")
            if answer == "Y" or answer == "y":
                os.system("clear")
                question1(name)
            elif answer == "N" or answer == "n":
                print("Alright! Press Enter to continue!")
                enter = input()
                os.system("clear")
    elif question_num == 2:
        if answer == "A" or answer == "a":
            print(f"Congrats {name}! That's correct.")
            print("Press Enter to continue!")
            enter = input()
            os.system("clear")
        else:
            print(f"Oh no! That's incorrect.")
            answer = input("Would you like to try again? Y/N ")
            if answer == "Y" or answer == "y":
                os.system("clear")
                question2(name)
            elif answer == "N" or answer == "n":
                print("Alright! Press Enter to continue!")
                enter = input()
                os.system("clear")
    elif question_num == 3:
        if answer == "C" or answer == "c":
            print(f"Congrats {name}! That's correct.")
            print("Press Enter to continue!")
            enter = input()
            os.system("clear")
        else:
            print(f"Oh no! That's incorrect.")
            answer = input("Would you like to try again? Y/N ")
            if answer == "Y" or answer == "y":
                os.system("clear")
                question3(name)
            elif answer == "N" or answer == "n":
                print("Alright! Press Enter to continue!")
                enter = input()
                os.system("clear")

def End(name):
    print("Congratulations!")
    print(f"Thank you for playing, {name}!")
    print("I will come back with more questions in the near future.")
    print("I hope you give the other games a try!")
    print("         __              ")
    print(" _(\    |..|             ")
    print("(__/\__ \--/ __          ") #robot ascii: https://www.asciiart.eu/electronics/robots
    print("   \___|----|  |   __    ")
    print("       \ }{ /\ )_ / _\   ")
    print("       /\__/\ \__O (__   ")
    print("      (--/\--)    \__/   ")
    print("      _)(  )(_           ")
    print("     `---''---`          ")
    print("-MathBot")
    return ("Bye!")

if __name__ == "__main__":
    main()