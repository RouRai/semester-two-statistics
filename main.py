import matplotlib.pyplot as plt
import pandas as pd

dataframe = pd.read_csv("variables_check.csv")

plt.scatter(dataframe["Life expectancy "], dataframe["Adult Mortality"])
plt.show()

