# Exchange Rates Analysis and Prediction
<p>
In this project, I analyse exchange rate changes and attempt to create a model predicting future rates. I extract data from an API and process it in Python using libraries such as 'requests', 'pandas', and 'matplotlib' among others. 
</p>
<p>
As a disclaimer, I am well aware that exchange rate prediction is an incredibly complex entreprise that even the most trained finance analysts struggle to undertake successfully. For this reason, my efforts to build a predictive model is not meant to guide consequential investment decisions. Rather,  it is a 'hands-on' attempt to learn essential skills and use key tools used in data analysis, applied to a problem that affects my everday life. 
</p>

## Rationale
<p>
As an expatriate student - first in London and now in Washington D.C.- my family supports me by regularly sending money. This money, earned in euros is subject to the fluctutions of exchange rates. Finding the correct window of opportunity, where exchange rates are optimal, can save a consequential amount of money. At this game, my father has essentially played a guessing name up until now. 
</p>
My objective is to inform his decision making in order to optimise those transfers and therefore save money. Additionally, predicting exchange rates could also be helpful in the budgeting of my family's worldwide travels. 

## Explore exchange rates fluctuations
### Pulling the exchange rates
#### Finding the right API
At the basis of this project is data extracted from the web using an API. The criteria guiding the choice of this API include: <br/>
1. Coverage of most major global currencies
2. Real-time updates
3. High number of API calls allowed / month for a reasonable price
4. Ease of use & in-depth documentation

<p>
The [Fixer.io](https://fixer.io/) API fulfilled those criteria best according to me. It is powered by 15+ exchange rate data sources, including the European Central Bank. It can deliver real-time exchange rate data for [170 world currencies](https://fixer.io/symbols).
</p>
<p>
Importantly, it comes with different functionalities allowing to get the latest exchange rate data for all or a specific set of currencies, retrieve time-series data and querying the API for daily fluctuation data. Those functionalities can be accessed by altering the API call's url, and will be used in the diversity of tasks performed in this project
</p>

A few limits of this API should be underlined:
1. The range of the timeframe when retriving time-series data is limited to a year. Analysing changes in exchange rates over a perdiod longer than a year will require the aggregation of different API calls. 
2. My subscription allows for a maximum of 300 daily requests. Although it is enough to perform most tasks for a project of this size, it did prompt require me to work around it in some cases as we will see later.

#### The get_rate() function


### Studying the fluctuations of exchange rates

## Predicting exchange rates changes

### ARIMA model: use historical data
Analysis of time series - but LIMITATIONS

### Include other dependent variables: use EDA takeawaya

## Potential follow-ups


## Personal takeaways of this project

### Skills developed 
first personal project in Python

### Thinking as a data analyst
