
# coding: utf-8

# In[42]:

import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint
import Street_Audit3

OSMFILE = "oshawa.osm"
num_line_street_re = re.compile(r'\d0?(st|nd|rd|th|)\s(Line)$', re.IGNORECASE) # Spell lines ten and under
nth_re = re.compile(r'\d\d?(st|nd|rd|th|)', re.IGNORECASE)
nesw_re = re.compile(r'\s(North|East|South|West)$')
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)

expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", 
            "Lane", "Road", "Way", "Trail", "Parkway", "Commons", "Circle", "Terrace", "Highway"]



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
    
def audit_street_types(street_types,streetname):
    m = street_type_re.search(streetname)
    if m:
        street_type = m.group()
        if street_type == mapping.keys():
            street_type == mapping['street_type']
        if street_type in expected:
            street_types[mapping.keys()].add(streetname)
        else:
            expected.extend(street_type)
            street_types[street_type].add(streetname)
            

# update street name according to the mapping dictionary
def fix_street(osmfile):
    st_types = Street_Audit3.audit_street(osmfile)
    for st_type, ways in st_types.items():
        for name in ways:
            if st_type in mapping:
                better_name = name.replace(st_type, mapping[st_type])
                print (name, "=>", better_name)
    

# Checking what other values to be added to the Mapping dictionary
def countthem(my_dict):
    for k,v in my_dict.items():
        print (k, len(list(filter(None, v))))


# In[43]:

#print (countthem(fix_street(OSMFILE)))



# In[ ]:



