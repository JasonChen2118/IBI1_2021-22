import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

print(os.getcwd())
print(os.listdir())
covid_data = pd.read_csv("full_data(2).csv")
print(covid_data.head(5))
print(covid_data.info())
print(covid_data.describe(), "\n")
print(covid_data.iloc[0, 1], "\n")
print(covid_data.iloc[2, 0:5], "\n")
print(covid_data.iloc[0:2, :], "\n")
print(covid_data.iloc[0:10:2, 0:5], "\n")
print(covid_data.iloc[0:3, [0, 1, 3]], "\n")

my_columns = [True, True, False, True, False, False]
print(covid_data.iloc[0:3, my_columns], "\n")

print(covid_data.loc[2:4, "date"], "\n")

print(covid_data.loc[0:81, "total_cases"], "\n")

row = []
for i in range(len(covid_data)):
    if covid_data.iloc[i, 1] == "Afghanistan":
        row.append(i)
row.append(row[-1] + 1)
print(covid_data.iloc[row[0]: row[-1], 0:5])

row = []
for i in range(len(covid_data)):
    if covid_data.iloc[i, 1] == "China":
        row.append(i)
row.append(row[-1] + 1)
china_new_data = covid_data.iloc[row[0]: row[-1], [0, 2, 3]]
print(china_new_data)

# mean = np.array(china_new_data)
print(np.mean(china_new_data.iloc[:, 1]))
print(np.mean(china_new_data.iloc[:, 2]))

plt.boxplot(china_new_data.iloc[:, 1], vert=True, whis=1.5, patch_artist=True, showbox=True, showcaps=True,
            showfliers=True)
plt.show()
plt.boxplot(china_new_data.iloc[:, 2], vert=True, whis=1.5, patch_artist=True, showbox=True, showcaps=True,
            showfliers=True)
plt.show()

china_dates = china_new_data.iloc[:, 0]
china_new_cases = china_new_data.iloc[:, 1]
china_new_death = china_new_data.iloc[:, 2]
plt.plot(china_dates, china_new_cases, 'b')
plt.plot(china_dates, china_new_death, 'r')
plt.xticks(china_dates.iloc[0:len(china_dates):4], rotation=-90)
plt.show()
