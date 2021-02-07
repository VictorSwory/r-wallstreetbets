#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd
import matplotlib
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from wordcloud import WordCloud, STOPWORDS
import warnings
warnings.simplefilter("ignore")


# In[4]:


data_df = pd.read_csv("/Users/VRodrigues/Documents/reddit_wsb.csv")


# In[5]:


data_df.head()


# In[6]:


data_df.info()


# In[9]:


def missing_data(data):
    total = data.isnull().sum()
    percent = (data.isnull().sum()/data.isnull().count()*100)
    tt = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
    types = []
    for col in data.columns:
        dtype = str(data[col].dtype)
        types.append(dtype)
    tt['Types'] = types
    return(np.transpose(tt))


# In[10]:


missing_data(data_df)


# In[15]:


def show_wordcloud(data, title=""):
    text = " ".join(t for t in data.dropna())
    stopwords = set(STOPWORDS)
    stopwords.update(["t", "co", "https", "amp", "U", "fuck", "fucking","retard", "new", "will", "buy", "time","stock"])
    wordcloud = WordCloud(stopwords=stopwords, scale=4, max_font_size=50, max_words=500,background_color="black").generate(text)
    fig = plt.figure(1, figsize=(16,16))
    plt.axis('off')
    fig.suptitle(title, fontsize=20)
    fig.subplots_adjust(top=2.3)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.show()


# In[16]:


show_wordcloud(data_df['title'], title = 'Prevalent words in titles')


# In[17]:


show_wordcloud(data_df['body'], title = 'Prevalent words in post bodies')


# In[ ]:




