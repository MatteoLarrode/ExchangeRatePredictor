import pandas as pd
import matplotlib.pyplot as plt

from rates import print_rates
from fluctuations import get_fluctuations_agg

print_rates("JPY", "USD", 90)


fluctuations_history = get_fluctuations_agg("USD", "EUR", 30, 3)
