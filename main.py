import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv("variables_check.csv")
dataframe = pd.DataFrame(dataframe, columns=['Life Expectancy', 'Adult Mortality'])

print(dataframe.sample(n=18))

plt.scatter(x=dataframe['Life Expectancy'], y=dataframe['Adult Mortality'])
plt.show()
