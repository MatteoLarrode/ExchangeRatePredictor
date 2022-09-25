#from rates import print_rates
#from rates2 import print_rates_double
from fluctuations import get_fluctuations_agg

#print_rates("USD", "EUR", 90)

fluctuations_history = get_fluctuations_agg("USD", "EUR", 30, 3)
print(fluctuations_history)