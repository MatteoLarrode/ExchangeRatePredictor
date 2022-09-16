import pandas as pd
import matplotlib.pyplot as plt
import datetime
import requests

#from config import api_key

def get_rates(base, currency1, amount_of_days, end_day = None):

  #if end date provided: turn it into datetime format
  if end_day is not None:
    end_date = datetime.datetime.strptime(end_day, '%m-%d-%Y').date()

  else:
      end_date = datetime.datetime.now().date()
  
  #set start date
  start_date = (end_date - datetime.timedelta(days = 1 * amount_of_days))

  url = "https://api.apilayer.com/fixer/timeseries?start_date=%s&end_date=%s&symbols=%s&base=%s" %(start_date, end_date, currency1, base)
  payload = {}
  headers= {"apikey": "A2YX3jHkSDGg8HwEFTK7N6jmHq6a93VN"}

  response = requests.request("GET", url, headers=headers, data = payload).json()
  
  #store data
  rate_history = {}
  rate_list = []

  for item in response['rates']:
    current_date = item
    currency1_rate = response['rates'][item][currency1]

    rate_history[current_date] = currency1_rate
    rate_list.append(currency1_rate)

  #get in pandas DF
  pd_result = pd.DataFrame([rate_history]).transpose()
  pd_result.columns = ["Rate"]

  #quick data viz
  plt.plot(rate_list)
  plt.ylabel(f"{base} to {currency1}")
  plt.xlabel("Days")
  plt.title (f"Value of exchange rate of {base} to {currency1} from {start_date} to {end_date}")
  plt.show()


get_rates("USD", "EUR", 365)