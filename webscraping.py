# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 16:39:41 2016

@author: dimira
"""

import urllib2
from bs4 import BeautifulSoup

wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
page = urllib2.urlopen(wiki)
soup = BeautifulSoup(page)

soup.prettify()  #to see whole html document
soup.title.string # to print title string
soup.find_all("a") # we can tag a link using tag “<a>”, 
#to extract all the links within <a>

#To find all the links in the page
all_links=soup.find_all("a")
for link in all_links:
    link.get("href")

#find all tables
all_tables=soup.find_all('table')

#print the right table we want
right_table=soup.find('table', class_='wikitable sortable plainrowheaders')

A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]

# Generate list for table with length greater than 6
for row in right_table.findAll("tr"):
    cells = row.findAll('td')
    states=row.findAll('th')
    if len(cells)==6:
        A.append(cells[0].find(text=True))
        B.append(states[0].find(text=True))
        C.append(cells[1].find(text=True))
        D.append(cells[2].find(text=True))
        E.append(cells[3].find(text=True))
        F.append(cells[4].find(text=True))
        G.append(cells[5].find(text=True))

#import pandas to convert list to data frame

import pandas as pd

df=pd.DataFrame(A,columns=['Number'])
df['State/UT']=B
df['Admin_Capital']=C
df['Legislative_Capital']=D
df['Judiciary_Capital']=E
df['Year_Capital']=F
df['Former_Capital']=G

print df