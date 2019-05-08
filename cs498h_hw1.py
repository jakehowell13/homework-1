#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt


# In[3]:


data = pd.read_csv('Data_Entry_2017.csv')


# In[4]:


data.describe()


# In[5]:


data.head()


# In[6]:


findings = data['Finding Labels']
findings.nunique()


# In[7]:


age = data['Patient Age']
age.describe()


# In[8]:


age.hist( bins=[x*5 for x in range(20)] )


# In[9]:


findings.value_counts()


# In[10]:


set([ x for x in findings if '|' not in x ])


# In[ ]:




