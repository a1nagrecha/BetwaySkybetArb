# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 12:37:39 2020

@author: a1nag
"""


from selenium import webdriver
from bs4 import BeautifulSoup
import time 



driver = webdriver.Chrome()
#telling the webdriver to search the specific url
driver.get("https://sports.betway.com/en/sports/cat/ufc---martial-arts")

# waiting for the page to load - TODO: change
driver.implicitly_wait(10)
#retrieving page source and parsing it
data = driver.page_source
soup = BeautifulSoup(data, "html.parser")
#the following code which is commented is used if I want the odds from one or more specific events
#driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#ufc251 = driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[1]/div/div[2]/div[4]/div/div[2]/div/div[2]/div/div[2]/div[1]/div/div[1]/div[1]")
#coordinates = ufc251.location_once_scrolled_into_view # returns dict of X, Y coordinates
#driver.execute_script('window.scrollTo({}, {});'.format(coordinates['x'], coordinates['y']))
#ufc251.click()
#scrolls down the web page 
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(3)
#produces an array for the odds
oddt = []
#finds all the elements for the odds numbers 
odd = driver.find_elements_by_class_name("odds")
#for loop to put the odds into an array
for i in range(0,len(odd)):
    oddt.append(odd[i].text)
#finds all elements with the names of each fighter
f2 = driver.find_elements_by_css_selector('.teamNameFirstPart.teamNameAwayTextFirstPart')
f1 = driver.find_elements_by_css_selector('.teamNameFirstPart.teamNameHomeTextFirstPart')

#creates arrays for the fighters names 
f2t = []
f1t = []
f3t = []
#fills the arrays for the fighters nanes
for i in range(0,len(f2)):
    f2t.append(f2[i].text)
    f1t.append(f1[i].text)

for i in range(0,len(f2t)):
    f3t.append(f1t[i])
    f3t.append(f2t[i])
    
for i in range(0,len(oddt)-1):
    oddt[i] = oddt[i+1]    
s = ['cat', 'dog', 'rat', 'pat']
p = ['orange', 'nana', 'pear', 'kiwi']
i = s[2], "vs", p[1]
print(i)
    
driver.quit()