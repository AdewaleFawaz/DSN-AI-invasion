#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd 
#initialize list of lists 
data= [['Ayo', 10], ['imran', 15], ['chucks', 14]]
#Creat the pandas DataFrame from the list and adding column headers  

df = pd.DataFrame(data, columns = ['Name', 'Age'])
# print DataFrame
df


# In[5]:


data= {'Name' : ['Ayo', 'imran','chucks'],'Age' :[10,15, 14]}
df=pd.DataFrame(data)
df


# In[16]:


dict_data = {"State": ["Abia", "Adamawa", "Lagos", "Osun", "Rivers"],
            "Capital": [" Umuahia" ,"Yola" , "Ikeja" , "Osogbo", "Portharcourt"],
            "area": [6320, 36917,3445,9251,11077],
            "population": [2845380, 3178950, 9113605, 3416959, 5198605]}
df= pd.DataFrame(dict_data)
df


# In[18]:


csv_df= pd.read_csv('Desktop/FAWAZ.csv')
print(csv_df)


# In[ ]:




