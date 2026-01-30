import numpy as np
import matplotlib.pyplot as plt

y_data = np.random.randint(100000, 1000000, size = 25)
x_data = np.arange(2000, 2025)

"""
linestyle - used to define the line that is displayed
alpha - states the opacity of the line
"""

plt.title('Price of DogCoin')
plt.xlabel('Year')
plt.ylabel('Price')
plt.grid(color='lightblue', linestyle = '--', linewidth = 0.5, axis = 'y')
plt.grid(color='lightblue', linestyle = '--', linewidth = 0.5, axis = 'x')
# Line Plot
# plt.plot(x_data, y_data, color = 'black', linewidth = 0.75, alpha = 0.75)

# Scatter Plot
# plt.scatter(x_data, y_data, color = 'green', s = 50, marker = '*', alpha = 0.50)

# Bar Graph
# plt.bar(x_data, y_data, color = 'lavender')

# Histogram
# plt.hist(y_data, rwidth = 0.75, color = 'lightblue')

fig, ax = plt.subplots(nrows = 1, ncols = 2)
fig.suptitle('Plot 1')
ax[0].plot(x_data, y_data, color = 'lightgreen')

ax[1].bar(x_data, y_data, color = 'lavender')

plt.legend(title = "", shadow = True)
plt.show()