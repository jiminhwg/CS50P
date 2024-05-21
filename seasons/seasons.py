from datetime import date
import sys
import re
import inflect


def main():
    Date = print(get_date(input("Date of Birth: ")), "minutes")

def get_date(Date):
    p = inflect.engine() #https://pypi.org/project/inflect/

    if matches := re.search(r"([1-2]\d{3})-(0[1-9]|1[0-2])-(0[1-9]|1[0-9]|2[0-9]|3[0-1])", Date):
        current_age = date.today() - date(int(matches.group(1)), int(matches.group(2)), int(matches.group(3)))
        minutes = current_age.days * 24 * 60
        return p.number_to_words(minutes, andword = "").capitalize() #https://pypi.org/project/inflect/
    else:
        sys.exit("Invalid Date")

if __name__ == "__main__":
    main()