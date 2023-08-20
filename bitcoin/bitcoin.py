import requests
import sys
import json

if len(sys.argv)<2:
    sys.exit("Missing command-line argument")

try:
    n=float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
    print("Request Exception")
else:
    o=response.json()
    rate=float(o["bpi"]["USD"]["rate_float"])
    print(f"${n*rate:,.4f}")