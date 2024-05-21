import inflect

List_of_names = []

while True: #gets names as input and stores in list
    try:
        Name = input("Name: ")
        if Name[-1] in "abcdefghijklmnopqrstuvwxyz":
            List_of_names.append(Name)
            continue
        else:
            break
    except (IndexError, EOFError):
        break

#if names == 1
if len(List_of_names) == 1:
    print("Adieu, adieu, to", List_of_names[0])

elif len(List_of_names) == 2:
    print("Adieu, adieu, to", List_of_names[0], "and", List_of_names[1])

else:
    List_of_names[0] = "to " + List_of_names[0] #first name should have "to"
    List_of_names[-1] = "and " + List_of_names[-1] #last name should have "and"
    print("Adieu, adieu,", end = " ")
    for a in List_of_names[:-1]:
        print(a, end = ", ")
    print(List_of_names[-1])
