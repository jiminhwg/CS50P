def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 <= len(s) <= 6:
        if s[0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" and s[1] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            if len(s) > 2: #if the plate is greater than 2 digits
                for a in s:
                    if a == "," or a == "." or a == "?" or a == "!" or a == " ": #if theres a punctuation in the plate
                        return False
                    else:
                        continue

                if s[-1] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ": #if the last digit is a letter
                    for a in s[2:-1]:
                        if a in "0123456789": #if a number is in the middle
                            return False
                        else:
                            continue
                    return True #if all the digits are a letter

                elif s[-1] in "0123456789": #if the last digit is a number
                    for b in s[2:-1]:
                        if b in "0123456789":
                            if s[2] == "0":
                                return False
                            else:
                                continue
                        elif b in "ABCDEFGHIJKLMNOPQRSTUVWXYZ": #if a letter is in the middle
                            if s[s.index(b)+1] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                                continue
                            else:
                                if s[s.index(b)+1] in "0123456789" and s.index(b)+1 == len(s)-1:#next are numbers
                                    return False
                                else:
                                    continue
                        elif b in "0123456789":
                            continue
                    return True
            elif len(s) == 2:
                return True
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    main()