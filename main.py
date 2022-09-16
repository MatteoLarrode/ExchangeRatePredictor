import pandas as pd
import matplotlib as plt
import datetime
import requests

today_date = datetime.datetime.now().date()

def get_rates(base, currency1, amount_of_days, end_date = today_date):

  #set start date
  start_date = (end_date - datetime.timedelta(days = 1 * amount_of_days))

  url = "https://api.apilayer.com/fixer/timeseries?start_date=%s&end_date=%s&symbols=%s&base=%s" %(start_date, end_date, currency1, base)
  payload = {}
  headers= {"apikey": "A2YX3jHkSDGg8HwEFTK7N6jmHq6a93VN"}

  response = requests.request("GET", url, headers=headers, data = payload).json()
  
  print (response) 

get_rates("USD", "EUR", 10)