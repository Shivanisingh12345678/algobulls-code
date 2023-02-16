#!/usr/bin/env python
# coding: utf-8

# In[5]:


import requests
import datetime


# In[4]:


import matplotlib.pyplot as plt


# In[5]:


url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo'

r=request.get(url)
print(f"status code:{r.status_code}")
# In[7]:


dis_data = r.json()


# In[8]:


dis_dicts = dis_data['Time Series(Daily)']h
dis_dates,highs,lows = [],[],[]
for date in dis_dicts:
    dis_dates.append(datetime.strptime(date,'%y-%m-%d'))
    highs.append(float(dis_dicts[date]['2.high']))
    lows.append(float(dis_dicts[date]['3,low']))


# In[9]:


plt.style.use('seaborn')
fig,ax.plt.subplot()
ax.plot(dis_dates,highs,c+'red',alpha=0.6)
ax.plot(dis_dates,lows,c='blue',alpha=0.6)
ax.fill_between(dis_dates,high,lows,facecolor='blue',alpha=0.15)

#format plot
ax.set_title(f"Daily high and low stock prices-Last 100 Days\n({symbol}) ",fontsize 24)
ax.set_xlabel('',fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("price USD",fontsize=10)
ax.tick_params(axis='both',which='major',Labelsize=10)
plt.ylim(min(lows),max(highs))
plt.show


# In[ ]:




