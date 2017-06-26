
# coding: utf-8

# In[24]:

import xml.etree.cElementTree as ET
import pandas as pd
from collections import defaultdict
import re


# In[25]:

street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)


# In[26]:

expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", 
            "Lane", "Road", "Way", "Trail", "Parkway", "Commons", "Circle", "Terrace", "Highway"]


# In[27]:

# In this, we are adding street names to individual street types. Something like this. Dr: Wilson Dr, Wilbur Drive
        
def audit_street_types(street_types,streetname):
    m = street_type_re.search(streetname)
    if m:
        street_type = m.group()
        if street_type in expected:
            street_types[street_type].add(streetname)
        else:
            expected.extend(street_type)
            street_types[street_type].add(streetname)


# In[28]:

def audit_street(osmfile):
    osm_file = open(osmfile, "r")
    street_types = defaultdict(set)
    
    for event, elem in ET.iterparse(osm_file, events=("start",)):
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                # if the tag is a street
                if tag.attrib['k'] == "addr:street":
                    audit_street_types(street_types, tag.attrib['v'])
    osm_file.close()
    return street_types


# In[29]:

#filename = "Oshawa.osm"
#print (audit_street(filename))
#print expected


# #### Count Street Types

# In[44]:

def countstrtypes(street_types,streetname):
    m = street_type_re.search(streetname)
    if m:
        street_type = m.group()
        if street_type in street_types:
            street_types[street_type] += 1
        else:
            street_types[street_type] = 1

def count_street(osmfile):
    osm_file = open(osmfile, "r")
    street_types = defaultdict(set)
    
    for event, elem in ET.iterparse(osm_file):
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                # if the tag is a street
                if tag.attrib['k'] == "addr:street":
                    countstrtypes(street_types, tag.attrib['v'])
    osm_file.close()
    return street_types


# In[43]:

#filename = "Oshawa.osm"
#print (count_street(filename))


# In[ ]:



