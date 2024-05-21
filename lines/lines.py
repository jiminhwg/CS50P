import sys

try:
    if sys.argv[2].isdigit() == False:
        sys.exit("Too many command-line arguments")
except IndexError: #if there are less than 2 cmd arguments:
    try:
        if ".py" in sys.argv[1]:
            with open(sys.argv[1], "r") as file:
                lines = file.readlines()

            count = 0
            for eachline in lines:
                if eachline.lstrip().startswith("#"):
                    continue
                elif eachline.isspace():
                    continue
                else:
                    count +=1
            print(count)

        else:
            sys.exit("Not a Python file")
    except FileNotFoundError:
        sys.exit("File does not exist")
    except IndexError: #when nothing is given in the command line
        sys.exit("Too few command-line arguments")
