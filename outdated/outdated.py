months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12,
}

while True:
    try:
        date = input("Date: ")
        if "/" in date:
            new_date = [int(x) for x in date.split("/")]
            x, y, z = new_date #mm,dd,yy
            if x <= 12 and y <= 31: #mm <= 12 and dd <=31
                print(z, end = "-")
                print(f"{x:02}", end = "-")
                print(f"{y:02}")
                break
            else:
                continue
        elif "," in date:
            new_date = date.split(" ")
            x, y, z = new_date #september 8, 2020

            for a in y: #removing the comma
                if a == ",":
                    y = y.replace(a, "")
                else:
                    continue

            if x.title() in months: #if the month exists
                x = months[x.title()]
                if int(y) <= 31: #if the date is less than or equal to 31
                    print(z, end = "-")
                    print(f"{x:02}", end = "-")
                    print(f"{int(y):02}")
                    break
                else:
                    continue
            else:
                continue

    except:
        continue

