#!/usr/bin/env python
# coding: utf-8

# notebook de Rajeeva

# In[7]:


"Hello World!"


# In[8]:


my_list = [5, 10, 15, 20, 25, 30]
my_list


# - La somme des valeurs
# - La moyenne (arrondie à 2 décimales)
# - La valeur maximale
# - La valeur minimale
# 

# In[9]:


resultats = (
    sum(my_list),
    round(sum(my_list)/len(my_list), 2),
    max(my_list),
    min(my_list)
)
resultats


# In[11]:


get_ipython().run_line_magic('time', 'flights = pd.read_parquet("flights.parquet")')


# In[12]:


get_ipython().run_cell_magic('timeit', '-n 25 -r 20', 'df = flights.copy()\ndf = df[df["AIR_TIME"] > 0]\ndf["AIR_TIME_LOG"] = np.log(df["AIR_TIME"])\ndf.describe()\n')


# In[13]:


get_ipython().run_line_magic('lsmagic', '')


# In[15]:


get_ipython().run_line_magic('history', '-n 1-10')


# In[16]:


get_ipython().run_line_magic('who', '')



import pandas as pd
import time

start = time.time()
flights = pd.read_parquet("flights.parquet")
end = time.time()
print("Temps d'exécution :", end - start, "secondes")


