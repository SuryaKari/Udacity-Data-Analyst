
# coding: utf-8

# In[1]:

import xml.etree.cElementTree as ET
import pandas as pd
from collections import defaultdict
import re


# In[2]:

street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)
mapping = { "St": "Street",
            "St.": "Street",
            "street": "Street",
            "Ave": "Avenue",
            "Ave.": "Avenue",
            "Blvd": "Boulevard",
            "Blvd.": "Boulevard",
            "Boulavard": "Boulevard",
            "Rd": "Road",
            "Rd.": "Road",
            "RD": "Road",
            "Pl": "Place",
            "Pl.": "Place",
            "PKWY": "Parkway",
            "Pkwy": "Parkway",
            "Ln": "Lane",
            "Ln.": "Lane",
            "Dr": "Drive",
            "Dr.": "Drive",
            "Cres": "Crescent",
            "Ct" : "Court",
            "west" : "West",
            "w" : "West",
            "W" : "West",
            "e" : "East",
            "E" : "East",
            "n" : "North",
            "N" : "North",
            "S" : "South",
            "s" : "South",
            "Driver" : "Drive"
            }


# In[3]:

expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", 
            "Lane", "Road", "Way", "Trail", "Parkway", "Commons", "Circle", "Terrace", "Highway"]


# In[11]:

# In this, we are adding street names to individual street types. Something like this. Dr: Wilson Dr, Wilbur Drive
        
def audit_street_types(street_types,streetname):
    m = street_type_re.search(streetname)
    if m:
        street_type = m.group()
        if street_type in mapping.keys():
            street_type = mapping[street_type]
        if street_type in expected:
            street_types[street_type].add(streetname)
        else:
            expected.extend(street_type)
            street_types[street_type].add(streetname)


# In[12]:

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


# In[13]:

#filename = "Oshawa.osm"
#print (audit_street(filename))
#print expected


# #### Count Street Types

# In[16]:

def countstrtypes(street_types,streetname):
    m = street_type_re.search(streetname)
    if m:
        street_type = m.group()
        if street_type in mapping.keys():
            street_type = mapping[street_type]
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


# In[17]:

filename = "Oshawa.osm"
print (count_street(filename))


# In[ ]:



