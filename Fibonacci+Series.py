
# coding: utf-8

# # Practice 1: Testing timeit Magic command

# ## Fibonacci Series (Method 1)

# In[2]:

from math import sqrt

def fibol(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibol(n-1) + fibol(n-1)


# ## Fibonacci Series (Method 2)

# In[3]:

def fibol2(n):
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))


# #### Here we try to explain what args(*) and kwargs(**) are
# 
# Args and Kwargs : http://stackoverflow.com/questions/36901/what-does-double-star-and-star-do-for-parameters

# In[6]:

get_ipython().magic('timeit fibol(100)')


# In[ ]:

get_ipython().magic('timeit fibol2(100)')

