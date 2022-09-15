import requests

#from config import api_key

def latest_rates():
  url_latest="https://api.apilayer.com/fixer/latest?symbols=GBP,EUR&base=USD"
  payload = {}
  headers= {
  #"apikey": api_key
  "apikey": "A2YX3jHkSDGg8HwEFTK7N6jmHq6a93VN"
  }
  response_latest = requests.request("GET", url_latest, headers=headers, data = payload).json()

  print(response_latest)




def old_rates_2000():
  #exchange rates in 2000
  url_2000 = "https://api.apilayer.com/fixer/timeseries?start_date=2000-01-01&end_date=2000-12-31&symbols=GBP,EUR&base=USD"
  payload = {}
  headers= {
    "apikey": "A2YX3jHkSDGg8HwEFTK7N6jmHq6a93VN"
  }
  response_2000 = requests.request("GET", url_2000, headers=headers, data = payload).json()

  print(response_2000)
