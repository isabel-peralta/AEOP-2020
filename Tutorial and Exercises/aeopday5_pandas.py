# -*- coding: utf-8 -*-
"""AEOPDay5 - Pandas.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1k__HFxCwgEHTHy5bgF6HCM14fqURfJcr

# Part 1: Starting with Data Analysis
"""

import pandas as pd 
from google.colab import drive
df = pd.read_csv('survey_results_public.csv')
df.head(10)

#or df.tail(x) to show other part of data

#df.shape comes with error not sure what it wrong

#pd.set_option['display.max_columns', 85]

#error comes up as CallableDynamicDoc object is not subscriptable

pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)
### To display all data without elipses

schema_df= pd.read_csv('survey_results_schema.csv')

schema_df

"""# Part 2: DataFrame and Series Basics"""

import pandas as pd
df = pd.read_csv('survey_results_public.csv')
schema_df = pd.read_csv('survey_results_schema.csv')
pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)
df.head()

people = {
    "first": ["Corey", "Jane", "John"],
    "last": ["Shafer", "Doe", "Doe"],
    "email": ["CoreyMShafer@gmail.com", "JaneDoe@email.com", "JohnDoe@email.com"]
}

people['email'] #compare to 32, this brings out a list

import pandas as pd
df1 = pd.DataFrame(people)
df1 #prints out the rows and columns with the index on the side

df1['email'] #compare to 30, this brings back a series

type(df1['email'])

df1.email   #dot notation also valid instead of key notation, 
           #bracket better to weed out repititions

#to access multiple columns, list the columns you want, returning a dataframe
df1[['last', 'email']]

df1.columns

#how to find rows?
df1.iloc[[0, 1], 2] # integer location #pass an inner list to get multiple rows
                # outer bracket and column brings down columns no names just inegers

# loc also finds rows but gets back dataframe, can use names for columns
df1.loc[[0, 1], ['email', 'last']]
#columns display in order of list

#stack overflow dataset
df.columns

df['Hobbyist'].value_counts()

df.loc[0:2, 'Hobbyist']  #: is slicing and doesn't need brackets



"""# Video 3: Indexes - How to Set, Reset, and Use Indexes"""

people = {
    "first": ["Corey", "Jane", "John"],
    "last": ["Shafer", "Doe", "Doe"],
    "email": ["CoreyMShafer@gmail.com", "JaneDoe@email.com", "JohnDoe@email.com"]
}

import pandas as pd
df = pd.DataFrame(people)
df

df['email']

df.set_index('email', inplace = True)
df
# sets that column as index, but doesn't modify df original until inplace is used

df.index

df.loc['CoreyMShafer@gmail.com', 'last'] #now you can search by email but not by index number

df.iloc[0] #iloc still uses integer location

import pandas as pd
df = pd.read_csv('survey_results_public.csv', index_col = 'Respondent')
schema_df = pd.read_csv('survey_results_schema.csv')
pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)
df.head()

df.loc[1]

schema_df()