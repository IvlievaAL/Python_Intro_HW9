# Задача 40: Работать с файлом california_housing_train.csv, который находится в папке
# sample_data. Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population)

import pandas as pd


df = pd.read_csv("california_housing_train.csv")
df1 = df[df.population < 501] # ноль как нижняя граница не указан, т.к. население меньше 0 быть не может.
print(df1.median_house_value.mean())