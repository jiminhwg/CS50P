import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    if matches := re.search(r"^([1-9]|1[0-2]):?([0-5][0-9])?\s(AM|PM)\sto\s([1-9]|1[0-2]):?([0-5][0-9])?\s(AM|PM)$",s):
        hourstart = hour_24(int(matches.group(1)), matches.group(3))
        hourend = hour_24(int(matches.group(4)), matches.group(6))

        if matches.group(2):
            minutestart = minute_24(int(matches.group(2)))
            if matches.group(5):
                minuteend = minute_24(int(matches.group(5)))
                return (f"{hourstart:02}:{minutestart:02} to {hourend:02}:{minuteend:02}")
        else:
            return (f"{hourstart:02}:00 to {hourend:02}:00")

    raise ValueError

def hour_24(hour, APM):
    if hour == 12 and APM == "AM":
        return 0
    elif hour == 12 and APM == "PM":
        return hour
    elif 1 <= hour < 12 and APM == "AM":
        return hour
    elif APM == "PM":
        return hour+12
    else:
        raise ValueError

def minute_24(minutes):
    if minutes > 60:
        raise ValueError
    else:
        return minutes

if __name__ == "__main__":
    main()