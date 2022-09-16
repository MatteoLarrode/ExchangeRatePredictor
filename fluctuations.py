import pandas as pd
import datetime
import requests

#from config import api_key

def get_fluctuations(base, currency1, amount_of_days, end_day = None):

  #if end date provided: turn it into datetime format
  if end_day is not None:
    end_date = datetime.datetime.strptime(end_day, '%m-%d-%Y').date()

  else:
      end_date = datetime.datetime.now().date()
  
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

  print(fluctuation_pct)
  

get_fluctuations("USD", "EUR", 270, "11-13-2009")


"""

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

"""