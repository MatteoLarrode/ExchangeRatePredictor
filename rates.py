import datetime
from turtle import color
import requests
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import NullFormatter

from config import api_key

def print_rates(base, currency1, amount_of_days, end_day = None):

  #if end date provided: turn it into datetime format
  if end_day is not None:
    end_date = datetime.datetime.strptime(end_day, '%m-%d-%Y').date()

  else:
      end_date = datetime.datetime.now().date()
  
  #set start date
  start_date = (end_date - datetime.timedelta(days = 1 * amount_of_days))

  url = "https://api.apilayer.com/fixer/timeseries?start_date=%s&end_date=%s&symbols=%s&base=%s" %(start_date, end_date, currency1, base)
  payload = {}
  headers= {"apikey": api_key}

  response = requests.request("GET", url, headers=headers, data = payload).json()
  
  #store data
  rate_list = []
  rate_history = {}

  for item in response['rates']:
    current_date = item
    currency1_rate = response['rates'][item][currency1]

    rate_history[current_date] = currency1_rate
    rate_list.append(currency1_rate)


  #get in pandas DF
  df_result = pd.DataFrame([rate_history]).transpose()
  df_result.columns = ["Rate"]
 

  fig, ax = plt.subplots()
  fig.set_size_inches(10,5)

  plt.plot(df_result)
  ax.spines['right'].set_visible(False)
  ax.spines['top'].set_visible(False)

  ax.xaxis.set_major_locator(mdates.MonthLocator())
  ax.xaxis.set_minor_locator(mdates.MonthLocator(bymonthday= [10, 20]))
  #PROBLEM: considers as if today is first day: minor divide the month as expected BUT not on the right dates

  ax.xaxis.set_major_formatter(mdates.DateFormatter('%b-%Y'))
  #GETS THE DATE WRONG! WHY?
  #in date format: not string so OK
  
  plt.gcf().autofmt_xdate()

  
  plt.axhline(1, linestyle='dashed', lw = '1', color = 'red')
  plt.grid(axis='y', lw = '0.5')
  plt.xlabel("")
  plt.title (f"Value of exchange rate of {base} to {currency1} from {start_date} to {end_date}")
  plt.show()

  return
