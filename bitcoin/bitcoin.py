import requests
import sys

try:
    if sys.argv[1].isnumeric() or "." in sys.argv[1]: #if the input is a number

        number = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        o = number.json()

        new_dict = o.get("bpi")
        new_dict2 = new_dict.get("USD")
        new_dict3 = new_dict2.get("rate_float") #float value

        amount = (float(new_dict3) * float(sys.argv[1]))
        print(f"${amount:,.4f}")


    else:
        sys.exit("Command-line argument is not a number")
except (requests.RequestException, IndexError):
    sys.exit("Missing command-line argument")