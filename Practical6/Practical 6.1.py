# import matplotlib
# merge two lists into one dictionary
# print the dictionary
# draw a scatter plot

import matplotlib.pyplot as plt

paternal_age = [30, 35, 40, 45, 50, 55, 60, 65, 70, 75]
chd = [1.03, 1.07, 1.11, 1.17, 1.23, 1.32, 1.42, 1.55, 1.72, 1.94]
d = dict(zip(paternal_age, chd))
# I don't really understand what is the data structure of zip file
print(d)

x = paternal_age
y = chd
plt.scatter(x, y)
plt.xlabel('Paternal age')
plt.ylabel('Risk for CHD')
# extra labels to make it clear
plt.show()

print('The risk of CHD in the offspring of a father of 45 age is', d[45])
