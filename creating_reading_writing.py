# importing pandas 
import pandas as pd

# creating a matrix with yes and no
classification_matrix = pd.DataFrame({'Yes':[50,21],'No':[131,21]},index=['Yes','No'])

# Let's create a new repository
new_matrix = pd.DataFrame({'Bob':['I Liked it','It was aweful'],'Sue':['Pretty Good','Bad']}, index=['Product A','Product B'])

# Series

# Simple series
new_series = pd.Series([1,2,3,4,5])
# Creating a year series. This is where Series are really powerful with indexes
year_sales = pd.Series([30,45,50], index=['Sales_2018','Sales_2019','Sales_2020'], name='Product_A')

# Let's read some data from csv

fuel = pd.read_csv('/Users/bt/Documents/GITHUB/python_small/fuel.csv')

fuel.drop('Unnamed: 0', axis=1, inplace=True)


# Indexing basically of following types

# Both of the following operations are row first and column second
# iloc

# This will give us the first row

print(fuel.iloc[0:])

# This will gives us the first column

print(fuel.iloc[:,0])

# Let's select the last 5 rows 

print(fuel.iloc[-5:,])

# How about last 5 columnd

print(fuel.iloc[:,-5])

# Following argument will give us all rows where NumGears == 6

print(fuel.loc[fuel.NumGears == 6])

# Let's use two filtering options

# The following one is an AND option

print(fuel.loc[(fuel['NumGears'] < 6) & (fuel['EngDispl'] == 2.0)])

# The following is an OR option

print(fuel.loc[(fuel['NumGears'] <= 2) | (fuel['EngDispl'] == 2.0)])

# Let's use the same argument but this time we will search in "Transmission" and look for "AM6" and "M6"

print(fuel.loc[fuel.Transmission.isin(['AM6','M6'])])

# Let's see if we have any "Transmission" with "Non Null"

print(fuel.loc[fuel.Transmission.notnull()])

# Let's look at summary

print(fuel.describe().T)

# We can also do it for single variables

print(fuel['NumCyl'].describe().T)

# To see the list of unique items 

print(fuel['Transmission'].unique())

# Let's also look at the frequency of each individual values

print(fuel['Transmission'].value_counts())