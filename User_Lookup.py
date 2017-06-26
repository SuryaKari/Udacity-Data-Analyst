
# coding: utf-8

# In[2]:

import xml.etree.cElementTree as ET
from collections import defaultdict # What does this do


# In[8]:

def count_users(filename):
    users =defaultdict(int)
    for _,element in ET.iterparse(filename):
        if element.tag == "node":
            if element.attrib["uid"] in users:
                users[element.attrib["uid"]] +=1
            else:
                users[element.attrib["uid"]] = 1
    return users
        
        


# In[10]:

#filename= "oshawa.osm"
#print len(count_users(filename))


# In[ ]:



