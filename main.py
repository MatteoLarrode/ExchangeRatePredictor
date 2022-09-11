import requests
import json
from pprint import pprint

from config import api_key

#call latest exchange rates

url_latest="https://api.apilayer.com/fixer/latest?symbols=GBP&base=USD"
payload = {}
headers= {
  "apikey": api_key
}

response_latest = requests.request("GET", url_latest, headers=headers, data = payload).json()

print(response_latest)