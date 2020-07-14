# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import re
import time 
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import json
import requests 
from lxml import html


driver = webdriver.Chrome()
#telling the webdriver to search the specific url
driver.get("https://m.skybet.com/ufc-and-mma")

# waiting for the page to load - TODO: change
driver.implicitly_wait(10)
#retrieving page source and parsing it
data = driver.page_source
soup = BeautifulSoup(data, "html.parser")


link = driver.find_elements_by_class_name("split__title")
#close the cookie
driver.find_element_by_class_name("js-page__cookies-accept").click()
#finding elements to click to find the correct page, and waiting for each page to load
link = driver.find_elements_by_class_name("split__title")
wait = WebDriverWait(driver, 5)
wait.until(lambda ignore:
          driver.find_element_by_class_name("split__title").is_displayed()
         and driver.find_element_by_class_name("split__title").is_enabled()
        , "Element is clickable")
#time.sleep(2)
link[0].click()



link2 = driver.find_elements_by_class_name("cell-text__line")
link2[0].click()
#producing lists that hold odds and the respective names
odds_link = driver.find_elements_by_class_name("js-oc-price ")
names_link = driver.find_elements_by_class_name("cell-text__line")
names = []
odds = []
print('len ', len(link2))
for i in range(0,2):
   odds.append(odds_link[i].text)
   names.append(names_link[i].text)    
#returning to the original webpage
driver.execute_script("window.history.go(-1)")
for i in range(0, len(link2)-1):
    print(i)
    time.sleep(1)
    #wait.until(lambda ignore:
     #   driver.find_element_by_class_name("split__title").is_displayed()
      #  and driver.find_element_by_class_name("split__title").is_enabled()
       # , "Element is clickable")
    link = driver.find_elements_by_class_name("split__title")
    for x in range(0,len(link)-1):
        coordinates = link[x].location_once_scrolled_into_view # returns dict of X, Y coordinates
        driver.execute_script('window.scrollTo({}, {});'.format(coordinates['x'], coordinates['y']))
        link[x].click()
    time.sleep(1)
    #wait.until(lambda ignore:
     #          driver.find_element_by_class_name("cell-text__line").is_displayed()
      #         and driver.find_element_by_class_name("cell-text__line").is_enabled()
       #        , "Element is clickable")
    link2 = driver.find_elements_by_class_name("cell-text__line")
    coordinates = link2[i].location_once_scrolled_into_view # returns dict of X, Y coordinates
    driver.execute_script('window.scrollTo({}, {});'.format(coordinates['x'], coordinates['y']))
    link2[i].click()
   # time.sleep(1)
#producing lists that hold odds and the respective names
    odds1 = (driver.find_elements_by_class_name("js-oc-price "))
    names1 = (driver.find_elements_by_class_name("cell-text__line"))
    for n in range(0,len(names1)):
        odds.append(odds1[n].text)
        names.append(names1[n].text)
    driver.execute_script("window.history.go(-1)")
#print(names,' ',odds)

driver.quit()