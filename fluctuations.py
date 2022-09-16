import pandas as pd
import datetime
import requests

#from config import api_key

#get total fluctuation between two chosen dates
def get_fluctuations(base, currency1, amount_of_days, end_date):

  #set start date
  start_date = (end_date - datetime.timedelta(days = 1 * amount_of_days))

  url = "https://api.apilayer.com/fixer/fluctuation?start_date=%s&end_date=%s&symbols=%s&base=%s" %(start_date, end_date, currency1, base)
  payload = {}
  headers= {"apikey": "A2YX3jHkSDGg8HwEFTK7N6jmHq6a93VN"}

  response = requests.request("GET", url, headers=headers, data = payload).json()

  fluctuation_pct = {}
  fluctuation_abs = {}

  change_pct = response['rates'][currency1]['change_pct']
  change_abs = response['rates'][currency1]['change']

  fluctuation_pct[response['end_date']] = change_pct
  fluctuation_abs[response['end_date']] = change_abs

  return fluctuation_pct


# now aggregate fluctuations over a given period
def get_fluctuations_agg(base, currency1, interval, timeframe, end_day = None):
  
  #if end_date not provided: set it as today
  if end_day is not None:
    end_date = datetime.datetime.strptime(end_day, '%m-%d-%Y').date()

  else:
      end_date = datetime.datetime.now().date()

  fluctuations_history = {}
  fluctuations_list = []

  for i in range(timeframe):
    current_end_date = end_date - datetime.timedelta(i*interval)

    fluctuation_pct = get_fluctuations(base, currency1, interval, current_end_date)
    
    current_end_date_str = list(fluctuation_pct.keys())[0]
    fluctuations_history[current_end_date_str] = fluctuation_pct[current_end_date_str]
    fluctuations_list.append(fluctuation_pct[current_end_date_str])

  print(fluctuations_history)




"""
#get in pandas DF
pd_result = pd.DataFrame([rate_history]).transpose()
pd_result.columns = ["Rate"]

"""

get_fluctuations_agg("USD", "EUR", 183, 1)