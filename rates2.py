import datetime
import requests
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import NullFormatter

from config import api_key

def print_rates_double(base, currency1, currency2, amount_of_days, end_day = None):

  #if end date provided: turn it into datetime format
  if end_day is not None:
    end_date = datetime.datetime.strptime(end_day, '%m-%d-%Y').date()

  else:
      end_date = datetime.datetime.now().date()
  
  #set start date
  start_date = (end_date - datetime.timedelta(days = 1 * amount_of_days))

  url = "https://api.apilayer.com/fixer/timeseries?start_date=%s&end_date=%s&symbols=%s,%s&base=%s" %(start_date, end_date, currency1, currency2, base)
  payload = {}
  headers= {"apikey": api_key}

  response = requests.request("GET", url, headers=headers, data = payload).json()
  
  #store data
  rate_history = {}

  for item in response['rates']:
    current_date = item
    currency1_rate = response['rates'][item][currency1]
    currency2_rate = response['rates'][item][currency2]

    rate_history[current_date] = []
    rate_history[current_date].extend([currency1_rate, currency2_rate])

  time = []
  currency1_rate_list = []
  currency2_rate_list = []
  
  for key in rate_history:
    time.append(key)
    currency1_rate_list.append(rate_history[key][0])
    currency2_rate_list.append(rate_history[key][1])


  df_result = pd.DataFrame({"time": time, f"{currency1} Rate": currency1_rate_list, f"{currency2} Rate": currency2_rate_list})
  df_result["time"] = pd.to_datetime(df_result["time"])

  #plot exchange rates
  fig, ax = plt.subplots()
  fig.set_size_inches(10,5)

  plt.plot(df_result["time"], df_result[f"{currency1} Rate"], label=f"{currency1}")
  plt.plot(df_result["time"], df_result[f"{currency2} Rate"], label=f"{currency2}")
  plt.legend()
  
  ax.spines['right'].set_visible(False)
  ax.spines['top'].set_visible(False)
  ax.xaxis.set_major_locator(mdates.MonthLocator())
  ax.xaxis.set_minor_locator(mdates.MonthLocator(bymonthday= [10, 20]))
  ax.xaxis.set_major_formatter(mdates.DateFormatter('%b-%Y'))
  plt.gcf().autofmt_xdate()
  plt.grid(axis='y', lw = '0.5')
  plt.xlabel("")
  plt.title (f"Exchange rate of the {base}/{currency1} and {base}/{currency2} pairs and from {start_date} to {end_date}")
  plt.savefig('./images/rates2.png')
  plt.show()

  return