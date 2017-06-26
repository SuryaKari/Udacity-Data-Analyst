
# coding: utf-8

# In[37]:

import xml.etree.cElementTree as ET
import re
from collections import defaultdict


#filename = "oshawa.osm"


# """
# Your task is to explore the data a bit more.
# Before you process the data and add it into your database, you should check the
# "k" value for each "<tag>" and see if there are any potential problems.
# We have provided you with 3 regular expressions to check for certain patterns
# in the tags. As we saw in the quiz earlier, we would like to change the data
# model and expand the "addr:street" type of keys to a dictionary like this:
# 
# 
# {"address": {"street": "Some value"}}
# 
# 
# So, we have to see if we have such tags, and if we have any tags with
# problematic characters.
# 
# 
# Please complete the function 'key_type', such that we have a count of each of
# four tag categories in a dictionary:
#   "lower", for tags that contain only lowercase letters and are valid,
#   "lower_colon", for otherwise valid tags with a colon in their names,
#   "problemchars", for tags with problematic characters, and
#   "other", for other tags that do not fall into the other three categories.
# See the 'process_map' and 'test' functions for examples of the expected format.
# """

# In[38]:

lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')


# In[45]:

# check the "k" value for each "<tag>"
def key_type(element,keys):
    if element.tag == "tag":
        for elem in element.iter('tag'):
            if lower.search(elem.attrib['k']):
                keys['lower'] += 1
            if lower_colon.search(elem.attrib['k']):
                keys['lower_colon'] += 1
            if problemchars.search(elem.attrib['k']):
                keys['problemchars'] += 1
            else:
                keys['other'] +=1
            
    return keys
    


# In[46]:

def parse_map(filename):
    keys = {"lower":0,
            "lower_colon":0,
            "problemchars":0,
            "other":0}
    for _, element in ET.iterparse(filename):
        keys = key_type(element,keys)
    return keys


# In[47]:

# print parse_map(filename)


# In[ ]:



