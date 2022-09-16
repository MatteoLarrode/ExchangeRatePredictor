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
  return response_latest


def latest_year_rates():
  #exchange rates in 2022
  url_latest_year = "https://api.apilayer.com/fixer/timeseries?start_date=2022-01-01&end_date=2022-09-15&symbols=GBP,EUR&base=USD"
  payload = {}
  headers= {
    "apikey": "A2YX3jHkSDGg8HwEFTK7N6jmHq6a93VN"
  }
  response_latest_year = requests.request("GET", url_latest_year, headers=headers, data = payload).json()
  return response_latest_year


def latest_month_rates():
  #exchange rates last month
  url_latest_month = "https://api.apilayer.com/fixer/timeseries?start_date=2022-08-15&end_date=2022-09-15&symbols=GBP,EUR&base=USD"
  payload = {}
  headers= {
    "apikey": "A2YX3jHkSDGg8HwEFTK7N6jmHq6a93VN"
  }
  response_latest_month = requests.request("GET", url_latest_month, headers=headers, data = payload).json()

  return response_latest_month



def old_rates_2000():
  #exchange rates in 2000
  url_2000 = "https://api.apilayer.com/fixer/timeseries?start_date=2000-01-01&end_date=2000-12-31&symbols=GBP,EUR&base=USD"
  payload = {}
  headers= {
    "apikey": "A2YX3jHkSDGg8HwEFTK7N6jmHq6a93VN"
  }
  response_2000 = requests.request("GET", url_2000, headers=headers, data = payload).json()

  return response_2000



def day_rate():
  #exchange rates yesterday
  url_date = "https://api.apilayer.com/fixer/2022-09-14?symbols=EUR&base=USD"
  payload = {}
  headers= {
  "apikey": "A2YX3jHkSDGg8HwEFTK7N6jmHq6a93VN"
  }
  response_day = requests.request("GET", url_date, headers=headers, data = payload).json()
  
  return response_day