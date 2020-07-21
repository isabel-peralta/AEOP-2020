# -*- coding: utf-8 -*-
"""AEOPDay6MPLandPandasPracticeipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UymBYPhgSfk-CMmwG738hPZa41v-eOTY

# MatPlotLib Practice
"""

import matplotlib
from matplotlib import pyplot as plt
import pandas as pd

data = pd.read_csv('company_sales_data.csv')
data

month_number = data['month_number']
total_profit = data['total_profit']
plt.plot(month_number, total_profit, color='Red',linestyle = ':', marker = 'o')
plt.xlabel('Month')
plt.ylabel('Total Profit')

# FIND HOW TO PUT LEGEND 
plt.legend()

"""Part 3"""

plt.style.use('fivethirtyeight')
month_number = data['month_number']

facecream = data['facecream']
plt.plot(month_number, facecream, marker = 'o')

facewash = data['facewash']
plt.plot(month_number, facewash, marker = 'o')

toothpaste = data['toothpaste']
plt.plot(month_number, toothpaste, marker = 'o')

bathingsoap = data['bathingsoap']
plt.plot(month_number, bathingsoap, marker = 'o')

shampoo = data['shampoo']
plt.plot(month_number, shampoo, marker = 'o')

moisturizer = data['moisturizer']
plt.plot(month_number, moisturizer, marker = 'o')

plt.xlabel('Month')
plt.ylabel('facecream')
plt.legend()

"""Part 4"""

plt.scatter(data['month_number'], data['toothpaste'])
#plt.grid('-')
plt.grid('-')
plt.xlabel('Month Number')
plt.ylabel('Number of Toothpaste Sold')
plt.title('Number of Toothpaste Sold for Each Month')

"""Part 5"""

width = 0.45
plt.bar(month_number, facecream, width = width)
plt.bar(month_number + width, facewash, width = width)

"""Part 6"""

plt.bar(month_number, bathingsoap)

"""Part 7"""

bins = [100000, 200000, 250000, 300000, 350000, 400000, 450000]
plt.hist(data['total_profit'], bins = bins, edgecolor = 'black')
plt.title('Salary Distribution')
#how many bins are needed?
plt.show()

"""Part 8"""

toothpastetotal = data['toothpaste'].sum()
shampoototal = data['shampoo'].sum()
facecreamtotal = data['facecream'].sum()
facewashtotal = data['facewash'].sum()
bathingsoaptotal = data['bathingsoap'].sum()
moisturizertotal = data['moisturizer'].sum()

slices = [toothpastetotal, shampoototal, facecreamtotal, facewashtotal, 
          bathingsoaptotal, moisturizertotal]
labels = ['Toothpaste', 'Shampoo', 'Facecream', 'Facewash',
          'Bathing Soap', 'Moisturizer']          
plt.pie(slices, labels=labels, autopct = '%1.1f%%')
plt.title("Product Portion of Total Sales")
plt.show()

"""Part 9"""

plt.subplot(221)
plt.plot(data['month_number'],data['bathingsoap'])
plt.subplot(222)
plt.plot(data['month_number'],data['facewash'])
#plt.plot(month_number, bathingsoap, label = 'Bathing Soap')

"""Part 10"""

labels = ['month_number','shampoo','toothpaste','facecream','facewash','bathingsoap','moisturizer']
plt.stackplot(data['month_number'], data['shampoo'], data['toothpaste'], data['facecream'], data['facewash'], 
              data['bathingsoap'], data['moisturizer'], labels = labels)
plt.title("All product sales")
plt.legend(loc=('lower left'))
plt.show()

"""# Pandas Practice

Part One: COMPLETE
"""

import matplotlib
from matplotlib import pyplot as plt 
import pandas as pd
data1 = pd.read_csv('Automobile_data.csv')
data1.head(5)

data1.tail(5)

"""Part 2: unsure

Part 3: COMPLETE
"""

pricemax = data1['price'].max()
print(pricemax) #when looking for company, should return mercedes

data1.set_index('price', inplace = True)
data1

most_expensive = data1.loc[pricemax, 'company']
print(most_expensive)
print(pricemax)

"""Part 4: COMPLETE"""

data1.set_index('company', inplace = True)
data1

data1.loc['toyota']

"""Part 5: COMPLETE"""

import matplotlib
from matplotlib import pyplot as plt 
import pandas as pd
data1 = pd.read_csv('Automobile_data.csv')
#list_of_companies = data1['company']
list_of_companies = data1['company'].to_list()

print(list_of_companies)

alfa_romero = list_of_companies.count('alfa-romero')
print('Alfa Romeros:', alfa_romero)
audi = list_of_companies.count('audi')
print('Audis:', audi)
bmw = list_of_companies.count('bmw')
print('BMWs:', bmw)
chevrolet = list_of_companies.count('chevrolet')
print('Chevrolets:', chevrolet)
toyota = list_of_companies.count('toyota')
print('Toyotas:', toyota)
#and so on

"""Part 6: COMPLETE"""

data1.set_index('company', inplace = True)
data1

dftoyota = data1.loc['toyota']
dftoyota

toyotamax = dftoyota['price'].max()
print("Most Expensive Toyota:", toyotamax)

dfbmw = data1.loc['bmw']
bmwmax = dfbmw['price'].max()
print("Most Expensive BMW:", bmwmax)

dfvolvo = data1.loc['volvo']
volvomax = dfvolvo['price'].max()
print("Most Expensive Volvo:", volvomax)

"""Part 7: COMPLETE"""

toyota_avg_mileage = dftoyota['average-mileage'].sum() / toyota
print("Toyota Average Mileage:", toyota_avg_mileage)
#and so on for all companies

"""Part 8: COMPLETE"""

data1.set_index('price', inplace = True)
data1

"""Part 9: concatenate the two data frammes and create a key for each data frame"""

## Question 9
import pandas as pd

GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925 , 71400]}
cars1 = pd.DataFrame.from_dict(GermanCars)

japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500 , 58900]}
cars2 = pd.DataFrame.from_dict(japaneseCars)

carsdf = pd.concat([cars1, cars2], keys= ("German", "Japanese"))
print(carsdf)

"""Part 10: Merge two data grames and append the second data fram as a new column to the first data fram"""

## Question 10
import pandas as pd 

Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925 , 71400]}
car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182 , 160]}

pricedf = pd.DataFrame.from_dict(Car_Price)
horsepowerdf = pd. DataFrame.from_dict(car_Horsepower)

carsdf = pd.merge(pricedf, horsepowerdf, on = "Company")
carsdf