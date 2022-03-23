# import matplotlib
# input given marks
# sort marks
# print sorted marks
# draw a boxplot
# calculate the sum of marks
# calculate the average mark
# print the average mark

import matplotlib.pyplot as plt

marks = [45, 36, 86, 57, 53, 92, 65, 45]
print(sorted(marks))
# I merge the sorting step and printing step.

plt.boxplot(marks, vert=True, whis=1.5, patch_artist=True, meanline=True, showbox=True, showcaps=True, showmeans=True,
            showfliers=True,
            notch=False)
# showing the mean line
plt.show()

total = 0
for i in range(0, len(marks)):
    total = total + marks[i]
average = total / len(marks)
print('average mark =', average)
# The average mark is 59.875, so Rob failed this ICA
