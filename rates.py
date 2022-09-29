import datetime
import requests
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import NullFormatter

from config import api_key

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

  df_result = pd.DataFrame({"time": list(rate_history.keys()), "rate": list(rate_history.values())})
  df_result["time"] = pd.to_datetime(df_result["time"])

  return df_result


def print_rates(base, currency1, amount_of_days, end_day = None):
  df_result = get_rates(base, currency1, amount_of_days, end_day = None)

  #need local start & end day for plot title
  if end_day is not None:
    end_date = datetime.datetime.strptime(end_day, '%m-%d-%Y').date()
  else:
      end_date = datetime.datetime.now().date()
  start_date = (end_date - datetime.timedelta(days = 1 * amount_of_days))

  #plot exchange rates
  fig, ax = plt.subplots()
  fig.set_size_inches(10,5)

  plt.plot(df_result["time"], df_result["rate"])
  
  ax.spines['right'].set_visible(False)
  ax.spines['top'].set_visible(False)
  ax.xaxis.set_major_locator(mdates.MonthLocator())
  ax.xaxis.set_minor_locator(mdates.MonthLocator(bymonthday= [10, 20]))
  ax.xaxis.set_major_formatter(mdates.DateFormatter('%b-%Y'))
  plt.gcf().autofmt_xdate()
  plt.grid(axis='y', lw = '0.5')
  plt.xlabel("")
  plt.title (f"Exchange rate between {base} and {currency1} from {start_date} to {end_date}")
  plt.savefig('./images/rates.png')
  plt.show()

  return