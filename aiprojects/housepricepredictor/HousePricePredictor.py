#!/usr/bin/env python
# coding: utf-8

# In[3]:
import pandas as pd
from sklearn import linear_model

df = pd.read_csv("housepricesdataset.csv", sep = ";")

# In[5]:
# The following is the feature set
df[['area', 'roomcount', 'buildingage']]


# In[6]:
# Define liner regression model
reg = linear_model.LinearRegression()
reg.fit(df[['area', 'roomcount', 'buildingage']], df['price'])


# In[7]:
# Predict for 230 area, 4 rooms, and 10 years old
reg.predict([[230, 4, 10]])


# In[8]:
# Predict for 230 area, 6 rooms, and 0 years old
reg.predict([[230, 6, 0]])


# In[9]:
# Predict for 355 area, 3 rooms, and 20 years old
reg.predict([[355, 3, 20]])


# In[12]:
#Predict all at once
reg.predict([[230, 4, 10], [230, 6, 0], [355, 3, 20], [432, 10, 3]])


# In[13]:
reg.coef_


# In[14]:
reg.intercept_


# In[15]:
# Coefficients of multiple linear regression model
# y = a + b1X1 + b2X2 + b3X3...

a = reg.intercept_
b1 = reg.coef_[0]
b2 = reg.coef_[1]
b3 = reg.coef_[2]

x1 = 230
x2 = 4
x3 = 10

y = a + b1*x1 + b2*x2 + b3*x3

print(y)




