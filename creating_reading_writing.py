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