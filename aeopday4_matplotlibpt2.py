# -*- coding: utf-8 -*-
"""AEOPDay4 - MatPlotLibPt2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ndTnmlr2CX6MFu7cVcl2N7lWWJ4IFnGX

# MatPlotLib Cont.

Video 6: Histograms
"""

import matplotlib
import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

#ages = [18, 19, 21, 25, 26, 26, 30, 32, 38, 45, 55]

bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.hist(ages, bins = bins, edgecolor = 'black', log = True)
                                                  #answers expressed logarithmically
data = pd.read_csv('data6.txt')
ids = data['Responder_id']
ages = data['Age']

median_age = 29
color = '#fc4f30'

plt.axvline(median_age, color = color, label = 'Age Median')

plt.legend()

plt.title('Ages of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')

plt.tight_layout()

plt.show()

"""Video 7: Scatter Plots"""

import pandas as pd
import matplotlib
from matplotlib import pyplot as plt

plt.style.use('seaborn')
"""
x = [5, 7, 8, 5, 6, 7, 9, 2, 3, 4, 4, 4, 2, 6, 3, 6, 8, 6, 4, 1]
y = [7, 4, 3, 9, 1, 3, 2, 5, 2, 4, 8, 7, 1, 6, 4, 9, 7, 7, 5, 1]

colors = [7, 5, 9, 7, 5, 7, 2, 5, 3, 7, 1, 2, 8, 1, 9, 2, 5, 6, 7, 5]

sizes = [209, 486, 381, 255, 191, 315, 185, 228, 174,
         538, 239, 394, 399, 153, 273, 293, 436, 501, 397, 539] 

### rewatch part about color correspondence thing it didn't make too much sense #

plt.scatter(x, y, s=100, c= colors, cmap = 'Greens',
            edgecolor = 'black', sizes = sizes, linewidth = 1, alpha = 0.75)

cbar = plt.colorbar()
cbar.set_label('Satisfaction')
"""
data = pd.read_csv('data7.txt')
view_count = data['view_count']
likes = data['likes']
ratio = data['ratio']

plt.scatter(view_count, likes, c = ratio, cmap = 'summer',
            edgecolor = 'black', linewidth = 1, alpha = 0.75)
cbar = plt.colorbar()
cbar.set_label('Like/Dislike Ratio')
# eliminate the outlier making it look weird (outlier still exists)
plt.xscale('log')
plt.yscale('log')

plt.title('Trending YouTube Videos')
plt.xlabel('View Count')
plt.ylabel('Total Likes')

plt.tight_layout()

plt.show()

"""Video 8: Plotting Time Series Data"""

import pandas as pd
import matplotlib
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

plt.style.use('seaborn')

"""dates = [
    datetime(2019, 5, 24),
    datetime(2019, 5, 25),
    datetime(2019, 5, 26),
    datetime(2019, 5, 27),
    datetime(2019, 5, 28),
    datetime(2019, 5, 29),
    datetime(2019, 5, 30)
]

y = [0, 1, 3, 4, 6, 5, 7]

plt.plot_date(dates, y, linestyle='solid')

plt.gcf().autofmt_xdate() # realligns the dates listed to be tilted

date_format = mpl_dates.DateFormatter('%b, %d, %Y')
                                                    #makes the date show up month, day, year
plt.gca().xaxis.set_major_formatter(date_format)"""

data = pd.read_csv('data8.txt')
price_date = data['Date']
price_close = data['Close']

plt.plot_date(price_date, price_close, linestyle='solid')

plt.gcf().autofmt_xdate()

plt.title('Bitcoin Prices')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.tight_layout()

plt.show()

### Timestamp 11:30

"""Video 9: Plotting Live Data Real Time"""

import random
import matplotlib
import itertools
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

index = count()

def animate(i):
  x_vals.append(next(index))
  y_vals.append(random.randint(0, 5))

  plt.cla()
  plt.plot(x_vals, y_vals)
                        #get current figure         #one second
ani = FuncAnimation(plt.gcf(), animate, interval = 1000)

#plt.tight_layout()
#plt.show()


HTML(ani.to_html5_video())

"""Video 10: Subplots"""

import pandas as pd
import matplotlib
from matplotlib import pyplot as plt
from IPython.display import HTML
plt.style.use('seaborn')

data = pd.read_csv('data.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

plt.plot(ages, py_salaries, label='Python')
plt.plot(ages, js_salaries, label='JavaScript')

plt.plot(ages, dev_salaries, color='#444444',
         linestyle='--', label='All Devs')

plt.legend()

plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')

plt.tight_layout()

plt.show()

"""# Pandas Tutorial"""