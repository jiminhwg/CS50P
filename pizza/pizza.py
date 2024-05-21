import sys
from tabulate import tabulate
import csv

try:
    if sys.argv[2].isdigit() == False:
        sys.exit("Too many command-line arguments")
except IndexError: #if there are less than 2 cmd arguments:
    try:
        grid = []
        if ".csv" in sys.argv[1]:
            with open(sys.argv[1]) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    grid.append(row)
            print(tabulate(grid, headers='keys', tablefmt='grid')) #https://pypi.org/project/tabulate/
        else:
            sys.exit("Not a CSV file")
    except FileNotFoundError:
        sys.exit("File does not exist")
    except IndexError: #when nothing is given in the command line
        sys.exit("Too few command-line arguments")
