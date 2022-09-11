import requests
from pprint import pprint

from config import api_key

#call latest exchange rates

url_latest="https://api.apilayer.com/fixer/latest?symbols=GBP&base=USD"
payload = {}
headers= {
  "apikey": api_key
}

response_latest = requests.request("GET", url_latest, headers=headers, data = payload)

status_code = response_latest.status_code
result_latest = response_latest.text

print(result_latest)

with open("response.txt", "w") as f:
    f.write(result_latest)