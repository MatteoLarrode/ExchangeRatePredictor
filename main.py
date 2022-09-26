#from rates import print_rates
#from rates2 import print_rates_double
from fluctuations import get_fluctuations_agg


#print_rates("USD", "TND", 365, "03-30-2011")

#print_rates_double("USD", "EUR", "GBP", 360, "09-30-2009")

get_fluctuations_agg("USD", "JPY", 90, 13, "11-30-2010")
