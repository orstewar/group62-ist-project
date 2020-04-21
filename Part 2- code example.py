#!/usr/bin/env python
# coding: utf-8

# In[4]:


import requests
import json
import numpy as np
import matplotlib.pyplot as plt

player = input("Enter a Current Player's Name: ")
player = player.upper()
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
        name = name.upper()
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
birthcity = bio['people'][0]['birthCity']
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

import pandas as pd
from IPython.display import display

key = "79b7b35dbc0c4a1d80203525202104"

location = birthcity
format_type = 'json'
included = 'Yes'
start = '2019-01-01'
end = '2019-01-30'
params = {'key' : key , 'q' : location , 'Format' : format_type , 'includelocation' : included , 'date' : start, 'enddate' : end }
response = requests.get("https://api.worldweatheronline.com/premium/v1/weather.ashx", params = params)
weather = response.json()
mintemp = weather['data']['ClimateAverages'][0]['month'][0]['avgMinTemp_F']
maxtemp = weather['data']['ClimateAverages'][0]['month'][0]['absMaxTemp_F']
weather = weather['data']['ClimateAverages'][0]['month']
maxtemps = []
mintemps = []
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May' , 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
count = 0
for i in weather:
    maxtemps.append(weather[count]['absMaxTemp_F'])
    count+=1
count = 0
for i in weather:
    mintemps.append(weather[count]['avgMinTemp_F'])
    count+=1
data = pd.DataFrame( { 'Month' : months, 'MaxTemps' : maxtemps, 'MinTemps' : mintemps})
display(data)





height = [goals , assists , points]
bars = ('goals', 'assists', 'points')
y_pos = np.arange(len(bars))
plt.bar(y_pos, height)
plt.xticks(y_pos, bars)
plt.title(player + ' total points breakdown')
plt.show()

print(player)
print(f'Time On Ice: {time}')
print(f'Goals: {goals}')
print(f'Assits: {assists}')
print(f'Points: {points}')


# In[ ]:




