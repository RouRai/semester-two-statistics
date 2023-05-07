import matplotlib.pyplot as plt
import pandas as pd

dataframe = pd.read_csv("variables_check.csv")
dataframe = pd.DataFrame(dataframe, columns=['Life Expectancy', 'Adult Mortality'])

subset = dataframe.sample(n=18)

plt.scatter(x=subset['Life Expectancy'], y=subset['Adult Mortality'], c=subset['Life Expectancy'])
plt.show()