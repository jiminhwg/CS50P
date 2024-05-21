# MathBot -- CS50P Final Project
## Video Demo:
https://youtu.be/iQ6o6DDBoBw

## Project Description:
MathBot is a simple, short, and interactive console game that introduces elementary math in English to the user. It was created with the purpose of introducing mathematical word problems in English that helps the user practice their math and language skills and encouraging bilinguality among students. MathBot is unique in the sense that it doesn't score the user based on how well or badly they performed, instead, MathBot encourages the student to retry questions they get wrong until they get the right answer so that the user learns through their constant effort in solving the problems.

## Files
1. project.py -- contains 8 functions
   - 1 main()
   - 1 loading_screen() -- introduces MathBot to the user and takes in user input (name of the user)
   - 1 intro() -- mentions the rules of the game
   - 3 question() -- asks the word problems and asks for user input (answer of the user)
   - 1 answer_checker() -- checks if the inputted answer from question() is correct; if the answer is wrong, this function gives the user a choice to either retry the question until they get the right answer or skip the question
   - 1 End() -- ends the program

2. test_project.py -- tests 6 functions from project.py
   ```
   uses pytest -s test_project.py
   ```
   - test_loading_screen()
   - test_intro()
   - test_question1()
   - test_question2()
   - test_question3()
   - test_End()

## Pictures:
### Loading Screen
<img width="276" alt="Screenshot 2023-01-11 at 6 47 15 PM" src="https://user-images.githubusercontent.com/84829334/211774176-625d6dfd-5a63-4e62-be15-5998f2187089.png">

### Sample Question
<img width="1327" alt="Screenshot 2023-01-11 at 6 47 32 PM" src="https://user-images.githubusercontent.com/84829334/211774225-b5d03aaf-2e1c-4078-9624-405b0723268f.png">

### Ending Message
<img width="607" alt="Screenshot 2023-01-11 at 6 47 53 PM" src="https://user-images.githubusercontent.com/84829334/211773615-ad86c62f-1b08-449e-bb3c-87a4256ca919.png">

## Documentation:
- https://www.asciiart.eu/electronics/robots
- https://www.prodigygame.com/main-en/blog/math-word-problems/
- https://docs.pytest.org/en/7.1.x/how-to/capture-stdout-stderr.html

