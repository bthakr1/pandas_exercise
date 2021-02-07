# importing pandas 
import pandas as pd

# creating a matrix with yes and no
classification_matrix = pd.DataFrame({'Yes':[50,21],'No':[131,21]},index=['Yes','No'])

# Printing the matrix
print(classification_matrix)

# Let's create a new repository

new_matrix = pd.DataFrame({'Bob':['I Liked it','It was aweful'],'Sue':['Pretty Good','Bad']}, index=['Product A','Product B'])

# print the new matrix

print(new_matrix)

# Series
# Simple series
new_series = pd.Series([1,2,3,4,5])
# Printing the simple series
print(new_series)
# Creating a year series. This is where Series are really powerful with indexes
year_sales = pd.Series([30,45,50], index=['Sales_2018','Sales_2019','Sales_2020'], name='Product_A')
# Printing the year_sales
print(year_sales)