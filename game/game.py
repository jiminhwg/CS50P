import random

while True:
    try:
        print("Level:", end = " ")
        n = int(input())

        random_number = random.randint(1,n)
        break
    except:
        continue


while True:
    try:
        print("Guess:", end = " ")
        guess = int(input())

        if guess < random_number:
            print("Too small!")
            continue
        elif guess > random_number:
            print("Too large!")
            continue
        elif guess == random_number:
            print("Just right!")
            break
    except:
        continue