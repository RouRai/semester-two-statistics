import matplotlib.pyplot as plt
import pandas as pd

dataframe = pd.read_csv("variables_check.csv")
dataframe = pd.DataFrame(dataframe, columns=['Life Expectancy', 'Adult Mortality'])

plt.scatter(x=dataframe['Life Expectancy'], y=dataframe['Adult Mortality'], c=dataframe['Life Expectancy'])
plt.title("Life Expectancy vs. Adult Mortality")
plt.xlabel("Life Expectancy (years)")
plt.ylabel("Adult Mortality (per 100,000)")
plt.show()
