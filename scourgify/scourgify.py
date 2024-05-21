import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    List = []
    NewList = []
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                List.append({"name": row["name"], "house": row["house"]})
            for student in List:
                last,first = (student['name']).split(",")
                first = first.lstrip()
                house = student["house"]
                NewList.append({"first": first, "last": last, "house": house})

        with open(sys.argv[2], "w") as file:
            writer = csv.DictWriter(file, fieldnames = ["first", "last", "house"])
            writer.writeheader()

            for row in NewList:
                writer.writerow(row)

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")
