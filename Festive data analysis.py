# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 16:27:09 2023

@author: NightHacker and KitWalker21
"""

import numpy as np
import pandas as pd
import seaborn as sns

# import csv file
df = pd.read_csv('C:\Users\ANKUSH\Desktop\Data science projects\Sales analysis\Diwali Sales Data.csv', encoding= 'unicode_escape')
df.shape
df.head() #view the top 5 rows of the data
df.info #
df.drop(["Status", "unnamed1"], axis=1, inplace=True) #drop unrelated/blank columns
pd.isnull(df).sum() #check for null values
df.dropna(inplace=True) #drop null values
df['Amount'] = df['Amount'].astype('int') #Changed the data type of 'Amount' to INT
df.Amount.datatypes #Check the data type of 'Amount' column
df.columns  #Check the column names in the table
df.rename(columns = {'Occupation' : 'Cust_occupation'})
df.describe() #describe() method returns description of the data in the DataFrame (i.e. count, mean, std, etc)
df[['Age', 'Orders', 'Amount']].describe() # use describe() for specific columns

#EXPLORATORY DATA ANALYSIS
#Bar chart for count of Males and Female in the dataset
    
ax = sns.countplot(x='Gendcer', data = df)

for bars in ax.containers:
    ax.bar_label(bars)
    
#Bar chart for Gender vs Total amount spend by them
sales_generated = df.groupby(['Gender'], as_index = False)['Amount'].sum().sort_values(by='Amount', ascending = False)

sns.barplot(x = 'Gender', y = 'Amount', data = sales_generated)

#Bar char for Gender vs Total amount spent by them with the age categories included
ax = sns.countplot(data = df, x = 'Age Group', hue = 'Gender')

for bars in ax.containers:
    ax.bar_label(bars)

#Bar chart for Total Amount spent in comparion with the age group the customer falls into
sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Age Group',y= 'Amount' ,data = sales_age)

#Chart for the count of total number of order across the 10 states
sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Orders')

#Chart for the total amount/sales from top 10 states
sales_state = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_state, x = 'State',y = 'Amount')

#Chart showing the number of customers who are married and unmarried
ax = sns.countplot(data = df, x = 'Marital_Status')

sns.set(rc={'figure.figsize':(7,5)})
for bars in ax.containers:
    ax.bar_label(bars)
    
#Chart showing the number of customers who are married and unmarried along with the genders
sales_state = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(data = sales_state, x = 'Marital_Status',y= 'Amount', hue='Gender')

#Chart showing the count of customers occupation-wise
sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Occupation')

for bars in ax.containers:
    ax.bar_label(bars)
    
#Chart showing the Amount spent by the customers according to their occupation
sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Occupation',y= 'Amount')

#Number of orders according to the product categories
sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Product_Category')

for bars in ax.containers:
    ax.bar_label(bars)
    
#Amount spent by the customers in comparison to the product categories
sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_Category',y= 'Amount')

#
sales_state = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_ID',y= 'Orders')

#
fig1, ax1 = plt.subplots(figsize=(12,7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')

#Married women age group 26-35 yrs from UP, Maharastra and Karnataka working in IT, Healthcare and Aviation are more likely to buy products from Food, Clothing and Electronics category
