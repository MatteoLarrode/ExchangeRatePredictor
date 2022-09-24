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
<p>
My objective is to inform his decision making in order to optimise those transfers and therefore save money. Additionally, predicting exchange rates could also be helpful in the budgeting of my family's worldwide travels.
</p>

Skip the implementation details by clicking [here](#analyzing-exchange-rate-fluctuations)


## Explore exchange rates fluctuations (method)
### Pulling the exchange rates
#### Finding the right API
At the basis of this project is data extracted from the web using an API. The criteria guiding the choice of this API include: <br/>
1. Coverage of most major global currencies
2. Real-time updates
3. High number of API calls allowed / month for a reasonable price
4. Ease of use & in-depth documentation


The [Fixer.io](https://fixer.io/) API fulfilled those criteria best according to me. It is powered by 15+ exchange rate data sources, including the European Central Bank. It can deliver real-time exchange rate data for [170 world currencies](https://fixer.io/symbols). It also includes their historical values since 1999.
<p>
Importantly, it comes with different functionalities allowing to get the latest exchange rate data for all or a specific set of currencies, retrieve time-series data and querying the API for daily fluctuation data. Those functionalities can be accessed by altering the API call's url, and will be used in the diversity of tasks performed in this project
</p>

A few limits of this API should be underlined:
1. The range of the timeframe when retriving time-series data is limited to a year. Analysing changes in exchange rates over a perdiod longer than a year will require the aggregation of different API calls. 
2. My subscription allows for a maximum of 300 daily requests. Although it is enough to perform most tasks for a project of this size, it did prompt require me to work around it in some cases as we will see later.

#### The print_rate() function
<p>
This function makes the API call to fetch the exchange rate of every day in the time period specified by the user, and for a chosen pair of currencies. It then plots a graph showing the evolution of the exchange rate over the chosen time period.
</p>

Parameters of the function:
- 'base': base currency [e.g. 'USD']
- 'currency1': currency studied [e.g. 'EUR']
    - the currrency code must be included in quotation marks
    - the list of supported currency codes is available [here](https://fixer.io/symbols)
- 'amount_of_days': length of the time period examined in days [e.g. 30]
    - maximum = 365
- 'end_day' (optional): end of the time period examined [e.g. '07-03-2001']
    - if no end date is provided, it is assigned to the date at which the program is run
    - format (including the quotation marks): 'mm-dd-yyyy'

<p>
Potential follow-up: add support for more currencies simultaneously studied. 
</p>


### Exchange rate fluctuations
My exploratory data analysis is centered around the question: <br/>
**Which independent variables are the most influential in affecting exchange rates fluctuations?** <br/> 
In other words, what causes exchange rates to change. <br/>
To answer this question, and given the scope and rationale of this project, I will focus on remarkable fluctuations of exchange rates. And this on different levels:
- years: geopolitical evolutions affecting exch. rates over the course of decades
- months: major events that can affect exch. rates over months
- days: less significant incidents leading to small hiccups of exch. rates

#### The get_fluctuations_agg() function

This function is the cornerstone of my study of exchange rates fluctuations. It makes use of the '/fluctuation' endpoint of the API that returns the total change (absolute or in percent) of the exchange rate between two days within a year of one another.
<p>
By combining this functionality with a 'for' loop, the function returns a history of exchange rates fluctuations for any number of a time interval chosen by the user. For example, this interval can be 30 days, allowing to observe monthly fluctuations of the exchange rate. An interval of 1 gives the daily changes while inputting 365 allows to compare years.
</p>

Parameters of the function:
- 'base': base currency [e.g. 'USD']
- 'currency1': currency studied [e.g. 'EUR']
    - the currrency code must be included in quotation marks
    - the list of supported currency codes is available [here](https://fixer.io/symbols)
- 'interval': span of the time interval in days 
    - maximum = 365
- 'timeframe': number of time the interval is repeated
- 'end_day' (optional): end of the time period examined [e.g. '07/03/2001']
    - if no end date is provided, it is assigned to the date at which the program is run
    - format (including the quotation marks): 'mm-dd-yyyy'

<p>
Example of use: get_fluctuations_agg("USD", "EUR", 90, 6) will return the change of exchange rate between US dollar and euro at the end of every trimester over the last 2 years (= 6 trimesters).
</p>

<p>
The range of customization of this function is extremely broad. The possibility of analyzing fluctuations of exchange rates over years (although later than 1999), and in 170 currencies, could allow to study major political or economic events far outside of the scope of this project.
</p>

## Analyzing exchange rate fluctuations
### Over years
1) Overview <br/>
The exchange rate gives the relative value of a currency compared to another. Since the end of the Bretton Woods agreement in the 1970s, most countries adopted free-floating currencies, allowing exchange rates to adjust to economic and market developments. They play a vital role in a country's level of trade and, aside from factors such as interest rates and inflation, are among the most important determinants of a country's relative level of economic health. We will look at some of the major forces behind exchange rate movements:


- Differentials in Inflation: countries with higher inflation see their purchasing power decrease relative to other currencies. As a result they typically see depreciation in their currency against the currencies of their trading partners. A gradual and orderly currency depreciation improves a nation’s export competitiveness and may improve its trade deficit over time. However, if too abrupt and/or sizeable, it may scare foreign investors who will then pull portfolio investments out of the country, putting further downward pressure on the currency.


- Differentials in Interest Rates: When interest rates are high, foreign lenders in an economy will get a higher return relative to other countries. This attraction of foreign capital causes the exchange rate to rise: there is appreciation. However, the intricate relationship between interest rates and inflation complicates this simple reasoning. For example, central banks usually raise interest rates in response to rising inflation. But, if inflation rises too quickly, it can devalue a currency quicker than interest rates can compensate foreign investors.




- historical examples (Development of countries: China? India? Changes of regimes)

2) USD - EUR <br/>
- exchange rates over the last decade
- quick overview

### Over months

Zooming in a little <br/>

1) General examples <br/>
- historical examples (covid? wars? Arab Springs? Brexit?)

2) USD - EUR <br/>
- exchange rates over the last months / year
- quick overview


But what interests us in this project are smaller scale variations<br/>
We have data on the daily and want to use it to inform everyday life decisions<br/>
Let's have a look at fluctuations over days <br/>

### Over days

1) Interesting examples <br/>
- historical examples (tweets, events, elections)


2) USD - EUR: Biggest fluctuations recently <br/>


## Predicting exchange rates changes
Having had a broad overview of exchange rates fluctuations at different levels, we can draw lessons about the factors that influence exchange rates. 

### ARIMA model: use historical data
Analysis of time series - but LIMITATIONS

### Include other dependent variables: using EDA takeawaya

## Potential follow-ups


## Personal takeaways from this project

### Skills developed 
first personal project in Python

### Thinking as a data analyst
