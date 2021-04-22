#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from pandas_datareader import data as wb


# In[2]:


from scipy.stats import norm
import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


crypto = ['BTC-USD','ETH-USD','LTC-USD','XRP-USD','DOGE-USD']
data = pd.DataFrame()
for c in crypto:
    data[c] = wb.DataReader(c, data_source='yahoo', start='2019-1-1')['Adj Close']


# In[4]:


data


# In[5]:


#Utility functions for calculating Option Price
def d1(S, K, r, stdev, T):
    return (np.log(S/K) + (r + stdev ** 2 / 2) * T) / (stdev * np.sqrt(T))


# In[6]:


def d2(S, K, r, stdev, T):
    return (np.log(S/K) + (r - stdev ** 2 / 2) * T) / (stdev * np.sqrt(T))


# In[7]:


def BSM(S, K, r, stdev, T):
    return (S * norm.cdf(d1(S, K, r, stdev, T))) - (K * np.exp(-r * T) * norm.cdf(d2(S, K, r, stdev, T)))


# In[8]:


#Extracting Bitcoin data from Yahoo API
crypto = ['BTC-USD']
mydata = pd.DataFrame()
mydata[crypto] = wb.DataReader(crypto, data_source="yahoo", start="2019-1-1")['Adj Close']


# In[9]:


#Bitcoin current Price in USD
BTC_Price = (float)(mydata.iloc[-1])
BTC_Price


# In[10]:


#Plot of Bitcoin Price
mydata.plot(figsize=(10,6))


# In[11]:


log_returns = np.log(1 + mydata.pct_change())
log_returns


# In[12]:


stdev = log_returns.std() * 250 ** 0.5
stdev


# In[13]:


#Inputs for Black Scholes Model

#risk free interest rate(r)
r = 3.69

#Strike Price(K)
K = 80000

#Time to maturity(T)
T = 1


# In[14]:


d1(BTC_Price, K, r, stdev, T)


# In[15]:


d2(BTC_Price, K, r, stdev, T)


# In[16]:


Option_Price1 = (float)(BSM(BTC_Price, K, r, stdev, T))
Option_Price1 


# In[17]:


df = pd.DataFrame({'Bitcoin':['BTC_Price', 'Option_Price'], 'Price':[BTC_Price,Option_Price1]})
ax = df.plot.bar(x='Bitcoin', y='Price', rot=0)


# In[18]:


#Extracting Ethereum data from Yahoo API
crypto = ['ETH-USD']
mydata = pd.DataFrame()
mydata[crypto] = wb.DataReader(crypto, data_source="yahoo", start="2019-1-1")['Adj Close']


# In[19]:


#Ethereum current Price in USD
ETH_Price = (float)(mydata.iloc[-1])
ETH_Price


# In[20]:


#Plot of Ethereum Price
mydata.plot(figsize=(10,6))


# In[21]:


log_returns = np.log(1 + mydata.pct_change())
log_returns


# In[22]:


stdev = log_returns.std() * 250 ** 0.5
stdev


# In[23]:


#Inputs for Black Scholes Model

#risk free interest rate(r)
r = 2.75

#Strike Price(K)
K = 2300

#Time to maturity(T)
T = 1


# In[24]:


d1(ETH_Price, K, r, stdev, T)


# In[25]:


d2(ETH_Price, K, r, stdev, T)


# In[26]:


Option_Price2 = (float)(BSM(ETH_Price, K, r, stdev, T))
Option_Price2 


# In[27]:


df = pd.DataFrame({'Ethereum':['ETH_Price', 'Option_Price'], 'Price':[ETH_Price,Option_Price2]})
ax = df.plot.bar(x='Ethereum', y='Price', rot=0)


# In[28]:


#Extracting Litecoin data from Yahoo API
crypto = ['LTC-USD']
mydata = pd.DataFrame()
mydata[crypto] = wb.DataReader(crypto, data_source="yahoo", start="2019-1-1")['Adj Close']


# In[29]:


#Litecoin current Price in USD
LTC_Price = (float)(mydata.iloc[-1])
LTC_Price


# In[30]:


#Plot of Litecoin Price
mydata.plot(figsize=(10,6))


# In[31]:


log_returns = np.log(1 + mydata.pct_change())
log_returns


# In[32]:


stdev = log_returns.std() * 250 ** 0.5
stdev


# In[33]:


#Inputs for Black Scholes Model

#risk free interest rate(r)
r = 3.15

#Strike Price(K)
K = 240

#Time to maturity(T)
T = 1


# In[34]:


d1(LTC_Price, K, r, stdev, T)


# In[35]:


d2(LTC_Price, K, r, stdev, T)


# In[36]:


Option_Price3 = (float)(BSM(LTC_Price, K, r, stdev, T))
Option_Price3 


# In[37]:


df = pd.DataFrame({'Litecoin':['LTC_Price', 'Option_Price'], 'Price':[LTC_Price,Option_Price3]})
ax = df.plot.bar(x='Litecoin', y='Price', rot=0)


# In[38]:


#Extracting Ripple data from Yahoo API
crypto = ['XRP-USD']
mydata = pd.DataFrame()
mydata[crypto] = wb.DataReader(crypto, data_source="yahoo", start="2019-1-1")['Adj Close']


# In[39]:


#Ripple current Price in USD
XRP_Price = (float)(mydata.iloc[-1])
XRP_Price


# In[40]:


#Plot of Ripple Price
mydata.plot(figsize=(10,6))


# In[41]:


log_returns = np.log(1 + mydata.pct_change())
log_returns


# In[42]:


stdev = log_returns.std() * 250 ** 0.5
stdev


# In[43]:


#Inputs for Black Scholes Model

#risk free interest rate(r)
r = 2.25

#Strike Price(K)
K = 1.12

#Time to maturity(T)
T = 1


# In[44]:


d1(XRP_Price, K, r, stdev, T)


# In[45]:


d2(XRP_Price, K, r, stdev, T)


# In[46]:


Option_Price4 = (float)(BSM(XRP_Price, K, r, stdev, T))
Option_Price4 


# In[47]:


df = pd.DataFrame({'Ripple':['XRP_Price', 'Option_Price'], 'Price':[XRP_Price,Option_Price4]})
ax = df.plot.bar(x='Ripple', y='Price', rot=0)


# In[48]:


#Extracting Dogecoin data from Yahoo API
crypto = ['DOGE-USD']
mydata = pd.DataFrame()
mydata[crypto] = wb.DataReader(crypto, data_source="yahoo", start="2019-1-1")['Adj Close']


# In[49]:


#Dogecoin current Price in USD
DOGE_Price = (float)(mydata.iloc[-1])
DOGE_Price


# In[50]:


#Plot of Dogecoin Price
mydata.plot(figsize=(10,6))


# In[51]:


log_returns = np.log(1 + mydata.pct_change())
log_returns


# In[52]:


stdev = log_returns.std() * 250 ** 0.5
stdev


# In[53]:


#Inputs for Black Scholes Model

#risk free interest rate(r)
r = 1.15

#Strike Price(K)
K = 0.25

#Time to maturity(T)
T = 1


# In[54]:


d1(DOGE_Price, K, r, stdev, T)


# In[55]:


d2(DOGE_Price, K, r, stdev, T)


# In[56]:


Option_Price5 = (float)(BSM(DOGE_Price, K, r, stdev, T))
Option_Price5


# In[57]:


df = pd.DataFrame({'Dogecoin':['DOGE_Price', 'Option_Price'], 'Price':[DOGE_Price,Option_Price5]})
ax = df.plot.bar(x='Dogecoin', y='Price', rot=0)


# In[58]:


Current_Price = [BTC_Price, ETH_Price, LTC_Price, XRP_Price, DOGE_Price]
Option_Price = [Option_Price1, Option_Price2, Option_Price3, Option_Price4, Option_Price5]
index = ['Bitcoin', 'Ethereum', 'Litecoin', 'Ripple', 'Dogecoin']

df = pd.DataFrame({'Current Price': Current_Price, 'Option Price': Option_Price}, index = index)
ax = df.plot.bar(rot=0)

