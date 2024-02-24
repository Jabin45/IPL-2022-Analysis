#!/usr/bin/env python
# coding: utf-8

# # IPL - 2022 Analysis

# In[1]:


# importing the required libraries

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# In[2]:


import plotly.io as pio
pio.renderers.default ='notebook'


# In[ ]:





# In[ ]:





# In[4]:


# loaded the dataset

data = pd.read_csv('IPL 2022.csv.csv')


# In[86]:


data.head(2)


# ## Number of matches won by each team in ipl 2022

# In[5]:


figure = px.bar(
    x = data["match_winner"].value_counts().index,
    y = data["match_winner"].value_counts(),
    color = data["match_winner"].value_counts().index,
    title = "Number of matches won by each team"
)
figure.show()


# In[93]:


data['won_by'] = data['won_by'].map({'Wickets': 'Chasing',
                                    'Runs' : 'Defending'})
won_by = data['won_by'].value_counts()
label = won_by.index
counts = won_by.values

colors = ['#cdb4db','#a2d2ff']

chart = go.Figure(data=[go.Pie(labels = label, 
                               values = counts)]
)
chart.update_layout(title_text = "Number of matches won by defending or chasing")
chart.update_traces(hoverinfo = 'label+percent', 
                    textinfo = 'value', 
                    textfont_size = 30,
                    marker = dict(
                        colors = colors, line = dict(color = 'black', width = 3)))
chart.show()


# In[20]:


figure = px.bar(
    x =  data["best_bowling"].value_counts().index,
    y = data["best_bowling"].value_counts(),
    color = data["best_bowling"].value_counts(),
    title = "Best Blowers in IPL 2022"   
)
figure.update_xaxes(title_text = "Player Names")
figure.show()


# In[41]:


figure = px.bar(
    x = data["player_of_the_match"].value_counts().index,
    y = data["player_of_the_match"].value_counts(),
    color = data["player_of_the_match"].value_counts().index
    title = "Most Player of the Match titles"
)
figure.show()


# # Top run scorer in IPL 2022

# In[96]:


figure = px.bar(
    data,
    x = data["top_scorer"],
    y = data["highscore"],
    color = data["highscore"],
    title = "Top Run Scorer's"
)
figure.show()


# In[45]:


import matplotlib.pyplot as plt
import seaborn as sns


# # Distribution of score among first innings and second innings score

# In[46]:


figure = plt.hist(
    data["first_ings_score"], 
    bins = 20, 
    color = "dimgray", 
    alpha=0.5,
    label = "first_ings_score"
)
plt.hist(
    data["second_ings_score"],
    bins = 20, 
    color = "cornflowerblue",
    alpha=0.5,
    label = "second_ings_score"
)
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.legend()
plt.show()


# # Toss Analysis

# In[98]:


sns.countplot(
    x = "toss_decision",
    data = data,
    hue = "match_winner"
)
plt.xlabel("Toss Decisions")
plt.ylabel("Count")
plt.show()


# In[ ]:




