#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Name : ")
print("This is a CSV of more than 200 rows which has Covide data.")
print("The task is to find out top 5 the countries who are least affected by covid")
print("Another task is to find out top 5 the countries who has the maximum number of deaths")
print("Another task is to find out top 5 the countries who has the maximum number of active cases")


# In[10]:


#Covide Data 
import  numpy as np
import pandas as pd
from matplotlib import pyplot as plt


dataframe = pd.read_csv('covid19.csv')
df = dataframe.dropna()
df


# In[2]:


#Task 1 
#Sort the data as per total number of cases
df = pd.DataFrame(dataframe, columns =['Total Number of cases','Country'])
df.replace(" ", float("NaN"), inplace=True)

df = df.dropna()

sorted_df = df.sort_values(by=['Cases'])
sorted_df


# In[4]:


#Task 2
#Get top 5 countries who has the least number of cases and plot a bar graph

least_countrys_5 = sorted_df.tail(5)
print(least_countrys_5)

name = least_countrys_5['least cases']
cases = least_countrys_5['Number of Cases']

plt.xlabel("Country")
plt.xticks(rotation='vertical')
plt.ylabel("cases


label = name
value = cases
plt.bar(label, value,width=0.4, color=('red','yellow','green','pink','blue')) #bar-grap


# In[5]:


#Task 3
#Sort the data as per total number of deaths
df = pd.DataFrame(dataframe, columns =['Total Number of deaths','Country'])
df.replace(" ", float("NaN"), inplace=True)

df = df.dropna()

sorted_df = df.sort_values(by=['Deaths'])
sorted_df



# In[6]:


#Task 4
#Get top 5 countries who has the maximum number of deaths and plot a bar graph
max_countrys_5 = sorted_df.tail(5)
print(least_countrys_5)

name = max_countrys_5['max cases']
cases = max_countrys_5['Number of Cases']

plt.xlabel("Country")
plt.xticks(rotation='vertical')
plt.ylabel("cases")


label = name
value = cases
plt.bar(label, value,width=0.4, color=('red','yellow','green','pink','blue')) #bar-grap




# In[5]:


#Task 5
#Sort the data as per active cases
df = pd.DataFrame(dataframe, columns =['Total Number of active cases','Country'])
df.replace(" ", float("NaN"), inplace=True)

df = df.dropna()

sorted_df = df.sort_values(by=['active cases'])
sorted_df


# In[6]:


#Task 6
#Get top 5 countries who has the maximum number of active cases and plot a bar graph
active_cases_countrys_5 = sorted_df.tail(5)
print(active_cases_countrys_5)

name = active_cases_countrys_5['max cases']
cases = active_cases_countrys_5['Number of Cases']

plt.xlabel("Country")
plt.xticks(rotation='vertical')
plt.ylabel("active_cases")


label = name
value = cases
plt.bar(label, value,width=0.4, color=('red','yellow','green','pink','blue')) #bar-grap


# In[ ]:





# In[ ]:




