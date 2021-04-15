#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
import pandas as pd


# In[2]:


crypto=['BTC-USD','ETH-USD','XRP-USD','LTC-USD','DOGE-USD']
mydata=pd.DataFrame()
for t in crypto:
    mydata[t]=wb.DataReader(t,data_source='yahoo',start='2019-1-1')['Adj Close']


# In[3]:


mydata.info()


# In[4]:


mydata.head()


# In[5]:


mydata.tail()


# In[6]:


mydata.iloc[0]


# In[7]:


(mydata/mydata.iloc[0]*100).plot(figsize=(15,8));
plt.show()


# In[8]:


returns=(mydata/mydata.shift(1))-1
weights=np.array([0.20, 0.20, 0.20, 0.20, 0.20])


# In[9]:


annual_returns=returns.mean()*250
np.dot(annual_returns, weights)


# In[10]:


pfoloio_return=str(round(np.dot(annual_returns, weights),5)*100)+'%'
print (pfoloio_return)


# In[11]:


Bitcoin = wb.DataReader('BTC-USD',data_source='yahoo',start='2019-1-1')
Bitcoin.head()


# In[12]:


Bitcoin.tail()


# In[13]:


Bitcoin['simple_return'] = (Bitcoin['Adj Close']/Bitcoin['Adj Close'].shift(1))-1
print (Bitcoin['simple_return'])


# In[14]:


Bitcoin['simple_return'].plot(figsize=(15,10))
plt.show()


# In[15]:


avg_returns_daily=Bitcoin['simple_return'].mean()
avg_returns_daily


# In[16]:


print(str(round(avg_returns_daily,5)*100)+'%')


# In[17]:


avg_returns_annualy=Bitcoin['simple_return'].mean() * 250
avg_returns_annualy


# In[18]:


print(str(round(avg_returns_annualy,5)*100)+'%')


# In[19]:


Ethereum = wb.DataReader('ETH-USD',data_source='yahoo',start='2019-1-1')
Ethereum.head()


# In[20]:


Ethereum.tail()


# In[21]:


Ethereum['simple_return'] = (Ethereum['Adj Close']/Ethereum['Adj Close'].shift(1))-1
print (Ethereum['simple_return'])


# In[22]:


Ethereum['simple_return'].plot(figsize=(15,10))
plt.show()


# In[23]:


avg_returns_daily_ETH=Ethereum['simple_return'].mean()
avg_returns_daily_ETH


# In[24]:


print(str(round(avg_returns_daily_ETH,5)*100)+'%')


# In[25]:


avg_returns_annualy_ETH=Ethereum['simple_return'].mean() * 250
avg_returns_annualy_ETH


# In[26]:


print(str(round(avg_returns_annualy_ETH,5)*100)+'%')


# In[27]:


Ripple = wb.DataReader('XRP-USD',data_source='yahoo',start='2019-1-1')
Ripple.head()


# In[28]:


Ripple.tail()


# In[29]:


Ripple['simple_return'] = (Ripple['Adj Close']/Ripple['Adj Close'].shift(1))-1
print (Ripple['simple_return'])


# In[30]:


Ripple['simple_return'].plot(figsize=(15,10))
plt.show()


# In[31]:


avg_returns_daily_XRP=Ripple['simple_return'].mean()
avg_returns_daily_XRP


# In[32]:


print(str(round(avg_returns_daily_XRP,5)*100)+'%')


# In[33]:


avg_returns_annualy_XRP=Ripple['simple_return'].mean() * 250
avg_returns_annualy_XRP


# In[34]:


print(str(round(avg_returns_annualy_XRP,5)*100)+'%')


# In[35]:


Litecoin = wb.DataReader('LTC-USD',data_source='yahoo',start='2019-1-1')
Litecoin.head()


# In[36]:


Litecoin.tail()


# In[37]:


Litecoin['simple_return'] = (Litecoin['Adj Close']/Litecoin['Adj Close'].shift(1))-1
print (Litecoin['simple_return'])


# In[38]:


Litecoin['simple_return'].plot(figsize=(15,10))
plt.show()


# In[39]:


avg_returns_daily_LTC=Litecoin['simple_return'].mean()
avg_returns_daily_LTC


# In[40]:


print(str(round(avg_returns_daily_LTC,5)*100)+'%')


# In[41]:


avg_returns_annualy_LTC=Litecoin['simple_return'].mean() * 250
avg_returns_annualy_LTC


# In[42]:


print(str(round(avg_returns_annualy_LTC,5)*100)+'%')


# In[43]:


Dogecoin = wb.DataReader('DOGE-USD',data_source='yahoo',start='2019-1-1')
Dogecoin.head()


# In[44]:


Dogecoin.tail()


# In[45]:


Dogecoin['simple_return'] = (Dogecoin['Adj Close']/Dogecoin['Adj Close'].shift(1))-1
print (Dogecoin['simple_return'])


# In[46]:


Dogecoin['simple_return'].plot(figsize=(15,10))
plt.show()


# In[47]:


avg_returns_daily_DOGE=Dogecoin['simple_return'].mean()
avg_returns_daily_DOGE


# In[48]:


print(str(round(avg_returns_daily_DOGE,5)*100)+'%')


# In[49]:


avg_returns_annualy_DOGE=Dogecoin['simple_return'].mean() * 250
avg_returns_annualy_DOGE


# In[50]:


print(str(round(avg_returns_annualy_DOGE,5)*100)+'%')


# In[ ]:




