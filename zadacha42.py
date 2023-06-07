# Задача 42: Узнать какая максимальная households в зоне минимального значения population

import pandas as pd


df = pd.read_csv("california_housing_train.csv")
df1 = df[df.population < df.population.quantile(0.25)]
print(df1.households.max())