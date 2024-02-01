# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 23:38:00 2024

@author: User
"""

#--- Read in dataset ----
import pandas as pd
#--- Read in dataset ----
df = pd.read_csv("C:/Users/User/Documents/DATAMINING6212/zomato.csv")

# ---WRITE YOUR CODE FOR TASK 1 ---
df.drop(['address', 'phone'], axis=1, inplace=True)

#--- WRITE YOUR CODE FOR TASK 2 ---
df.rename(columns ={'rate' :'rating', 'approx_cost(for two people)' :'approx_cost','listed_in(type)':'type',},inplace=True)

#--- Inspect data ---
print(df)

##--- WRITE YOUR CODE FOR TASK 3 ---

# Remove rows with null values in the 'name' column
df.dropna(subset=['name'], inplace=True)

# Fill null values in the 'online_order' column with 'NA'
df['online_order'].fillna('NA', inplace=True)

# Fill null values in the 'book_table' column with 'NA'
df['book_table'].fillna('NA', inplace=True)

# Replace null values in the 'rating' column with 0
df['rating'].fillna(0, inplace=True)

# Replace null values in the 'votes' column with 0
df['votes'].fillna(0, inplace=True)

# Fill null values in the 'location' column with 'NA'
df['location'].fillna('NA', inplace=True)

# Fill null values in the 'rest_type' column with 'NA'
df['rest_type'].fillna('NA', inplace=True)

# Fill null values in the 'dish_liked' column with 'NA'
df['dish_liked'].fillna('NA', inplace=True)

# Fill null values in the 'cuisines' column with 'NA'
df['cuisines'].fillna('NA', inplace=True)

# Replace null values in the 'approx_cost' column with 0
df['approx_cost'].fillna(0, inplace=True)

# Fill null values in the 'type' column with 'NA'
df['type'].fillna('NA', inplace=True)


#--- Inspect data ---
print(df)


#--- WRITE YOUR CODE FOR TASK 4 ---

# droping the duplicates value keeping the first
df.drop_duplicates(inplace=True, keep='first')

# Inspect the modified DataFrame
print(df)


#--- WRITE YOUR CODE FOR TASK 5 ---

# Remove rows where any of the specified columns contain 'RATED' or 'Rated'
df = df[df['name'].str.contains('RATED|Rated') == False]
df = df[df['type'].str.contains('RATED|Rated') == False]
df = df[df['approx_cost'].str.contains('RATED|Rated') == False]
df = df[df['cuisines'].str.contains('RATED|Rated') == False]
df = df[df['dish_liked'].str.contains('RATED|Rated') == False]
df = df[df['rest_type'].str.contains('RATED|Rated') == False]
df = df[df['location'].str.contains('RATED|Rated') == False]
df = df[df['votes'].str.contains('RATED|Rated') == False]
df = df[df['rating'].str.contains('RATED|Rated') == False]
df = df[df['book_table'].str.contains('RATED|Rated') == False]

# Inspect the modified DataFrame
print(df)

#--- WRITE YOUR CODE FOR TASK 6 ---
# online order table should have only yes and no, remove other values
df = df[df['online_order'].str.contains('Yes|No') == True]
# check for rating table and replace NEW,- values to 0 and remove /5
df['rating'].replace(to_replace='NEW', value=0, inplace=True)
df['rating'].replace(to_replace='-', value=0, inplace=True)
df['rating'].replace(to_replace=r'/5$', value='', regex=True, inplace=True)

#--- Inspect data ---
df

#--- WRITE YOUR CODE FOR TASK 7 ---
#df = ...
# remove unknown character from dataset
# Use regular expression to clean the 'name' column
df['name'] = df['name'].str.replace('[Ãx][^A-Za-z]+', '', regex=True)
df.to_csv('zomatocleaned.csv', index = False)

