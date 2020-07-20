# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import time 


driver = webdriver.Chrome()
#telling the webdriver to search the specific url
driver.get("https://m.skybet.com/ufc-and-mma")

# waiting for the page to load - TODO: change
driver.implicitly_wait(10)
#retrieving page source and parsing it
data = driver.page_source
soup = BeautifulSoup(data, "html.parser")


link = driver.find_elements_by_class_name("split__title")
#close the cookie, as it is in the way of a clickable element
driver.find_element_by_class_name("js-page__cookies-accept").click()
#finding elements to click to find the correct page, and waiting for each page to load
link = driver.find_elements_by_class_name("split__title")
#declaring variable that waits for a maximum of five seconds
wait = WebDriverWait(driver, 5)
#link2 holds all the elements associated with each bout
link2 = driver.find_elements_by_class_name("cell-text__line")
#delcaring array that will hold odds values and the respective names
names = []
odds = []
#for loop cycles through all the boats and adds odds and names to an array
for i in range(0, len(link2) - 1):
    print(i)
    #waits for split title element to be clickable
    wait.until(lambda ignore:
        driver.find_element_by_class_name("split__title").is_displayed()
        and driver.find_element_by_class_name("split__title").is_enabled()
        , "Element is clickable")
    link = driver.find_elements_by_class_name("split__title")
    #for loop clicks on every link to allow access to each element associated with "cell-text__line" elements
    for x in range(0,len(link)):
        coordinates = link[x].location_once_scrolled_into_view # returns dict of X, Y coordinates
        driver.execute_script('window.scrollTo({}, {});'.format(coordinates['x'], coordinates['y']))
        link[x].click()
    #waits for element to be clickable
    wait.until(lambda ignore:
               driver.find_element_by_class_name("cell-text__line").is_displayed()
               and driver.find_element_by_class_name("cell-text__line").is_enabled()
               , "Element is clickable")
    link2 = driver.find_elements_by_class_name("cell-text__line")
    #scrolls to the specific element, so it can be clicked
    coordinates = link2[i].location_once_scrolled_into_view # returns dict of X, Y coordinates
    driver.execute_script('window.scrollTo({}, {});'.format(coordinates['x'], coordinates['y']))
    link2[i].click()
#producing lists that hold odds and the respective names
    odds1 = (driver.find_elements_by_class_name("js-oc-price "))
    names1 = (driver.find_elements_by_class_name("cell-text__line"))
    for n in range(0,len(names1)):
        odds.append(odds1[n].text)
        names.append(names1[n].text)
    #goes back a web page so the start of the for loop can restart
    driver.execute_script("window.history.go(-1)")

driver.quit()