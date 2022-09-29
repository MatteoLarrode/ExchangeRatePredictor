import matplotlib.pyplot as plt
from prophet import Prophet

from rates import get_rates

#dataset: EUR/USD over the last year 
data = get_rates("EUR", "USD", 60)
data.columns = ['ds', 'y']

# input to Prophet is always a pandas.dataframe with two columns: ds and y. 
# The ds (datestamp) column should be of a format expected by Pandas, ideally YYYY-MM-DD for a date
def forecast(df, period, ci = 0.95):
    data = df

    #train model (5% confidence interval)
    m = Prophet(interval_width = ci, daily_seasonality=True)
    model = m.fit(data)

    #forecast away
    future = m.make_future_dataframe(periods = period,freq='D') #forecast every day over the next month
    forecast = m.predict(future)

    #PLOT
    #1)create new plot
    figsize=(10, 6)
    fig = plt.figure(facecolor='w', figsize=figsize)
    ax = fig.add_subplot(111)
    plt.title(f"Forecast exchange rates over the next {period} days [Confidence Interval: {ci*100}%]")

    #plot the black dots which indicate the data points used to train the model.
    fcst_t = forecast['ds'].dt.to_pydatetime()
    ax.plot(model.history['ds'].dt.to_pydatetime(), model.history['y'], 'k.')

    #plot predictions & confidence interval
    ax.plot(fcst_t, forecast['yhat'], ls='-', c='#0072B2')
    ax.fill_between(fcst_t, forecast['yhat_lower'], forecast['yhat_upper'], color='#0072B2', alpha=0.2)

    #save graph
    plt.savefig('./images/forecast.png')

    #plot compenents (different types of seasonality)
    model.plot_components(forecast)
    plt.savefig('./images/components.png')

    plt.show()

    return forecast


forecast_df = forecast(data, 10, 0.8)




