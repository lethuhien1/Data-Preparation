#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np
data = pd.read_csv("earthquakes.csv", sep = ',')
data.head()


# In[2]:


#Ex1: How many earthquake have magType 'ml' and type 'explosion'?
x = sum((data.type == 'explosion') & (data.magType == 'ml'))
x


# In[4]:


#Ex2: Calculate the mean of mag in Alaska and the distance is smaller than 100km, example: "62km W of Cantwell, Alaska".
y = data.mag[(data.place.str.contains('Alaska'))&~(data.place.str.contains('\d\d\d', na=False, regex=True))].mean()
y

