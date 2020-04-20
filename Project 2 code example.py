#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests
import json

player = input("Enter a Current Player's Name: ")
player = player.title()
endpoint = 'https://statsapi.web.nhl.com/api/v1/teams'
team = 1
count = 0
playerid = 'Name Not Found'
while True:
    url = f'{endpoint}/{team}/roster'
    response = requests.get(url)
    data = response.json()
    data = data['roster']
    for i in data:
        size = len(data)
        if count >= size:
            break
        name = data[count]['person']['fullName']
        if name == player:
            playerid = data[count]['person']['id']
            break
        else:
            count+=1
    team+=1
    if team == 11:
        team+=1
    if team == 27:
        team+=1
    if team == 31:
        team = team + 21
    if team == 55:
        break
    count = 0
playerid






playerid = playerid
endpoint = 'https://statsapi.web.nhl.com/api/v1/people/'
url = f'{endpoint}{playerid}'
response = requests.get(url)
bio = response.json()
birthcity = bio['person'][0]['birthCity']
birthcity


playerid = playerid
endpoint = f'https://statsapi.web.nhl.com/api/v1/people/{playerid}/stats?'
stattype = 'statsSingleSeason'
seasons = '20182019'
params = { 'stats' : stattype , 'season' : seasons}
response = requests.get(endpoint, params = params)
statistics = response.json()
statistics = statistics['stats'][0]['splits'][0]['stat']
time = statistics['timeOnIce']
goals = statistics['goals']
assists = statistics['assists']
points = statistics['points']
print(player)
print(f'Time On Ice: {time}')
print(f'Goals: {goals}')
print(f'Assits: {assists}')
print(f'Points: {points}')



# In[4]:


get_ipython().system('pip install --upgrade chart-studio plotly')


# In[5]:


get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib
import matplotlib.pyplot as plt
import chart_studio as plotly
import chart_studio.plotly as py
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import folium
import warnings
warnings.filterwarnings('ignore')


# In[ ]:




