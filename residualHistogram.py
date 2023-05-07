import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def linear_regression_line(x):
    return np.dot(x, -9.55369) + 824.283


dataframe = pd.read_csv("variables_check.csv")
dataframe = pd.DataFrame(dataframe, columns=['Life Expectancy', 'Adult Mortality'])

subset = dataframe.sample(n=18)
subset['Life Expectancy'] = [73.3, 64.5, 76.1, 61.4, 55.0, 66.1, 71.3, 72.0, 74.9, 51.0, 74.0, 61.8, 63.5, 79.0, 76.6,
                             52.4, 82.4, 58.9]
subset['Adult Mortality'] = [114, 293, 16, 259, 312, 227, 195, 13, 148, 413, 146, 33, 24, 159, 99, 335, 78, 373]

predicted = linear_regression_line(subset['Life Expectancy'])
residuals = subset['Adult Mortality'] - predicted

plt.hist(residuals, bins=[-225, -150, -75, 0, 75, 150])
plt.xlim(-200, 150)
plt.title("Histogram of Residuals")
plt.xlabel("Residual (Observed per 1000 persons - Expected per 1000 persons)")
plt.ylabel("Frequency of Residuals")
plt.show()
