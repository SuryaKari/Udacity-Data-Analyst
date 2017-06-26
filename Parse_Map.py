
# coding: utf-8

# #### Import Libraries

# In[11]:

import xml.etree.cElementTree as ET


# #### Count the total number of Tags

# In[15]:

def numberoftags(filename):
    tags= {}
    a = 0
    for events,elem in ET.iterparse(filename):
        if elem.tag in tags:
            a = a+1
            tags[elem.tag] = a
        else:
            a = 1
            tags[elem.tag] = a
    return tags

