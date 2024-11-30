from bs4 import BeautifulSoup

import requests
import lxml

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException

forms="https://docs.google.com/forms/d/e/1FAIpQLSd8sVZ1hctI64p_xtHtgSJ4Io9HkEqbE8l55A2guSmELcUyuQ/viewform?usp=sf_link"


response=requests.get(url="https://appbrewery.github.io/Zillow-Clone/")
print(response)
response_text=response.text

soup=BeautifulSoup(response_text,"lxml")
print(soup.title.getText())
price=soup.find_all(name="span",class_="PropertyCardWrapper__StyledPriceLine")
price_see=[i.getText().replace('/mo','').split('+')[0] for i in price]
print(price_see)

links=soup.find_all(name="a",class_="property-card-link",href=True)
links_see=[a['href'] for a in links]
# print(links_see)

address=soup.find_all(name="address")
address_see=[i.getText().strip().replace('|','') for i in address]
# print(len(address_see))

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=chrome_option)

for i in range(len(links_see)):
    driver.get(forms)
    time.sleep(5)
    q1=driver.find_element(By.XPATH,value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    q1.send_keys(address_see[i])
    time.sleep(2)
    q2=driver.find_element(By.XPATH,value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    q2.send_keys(price_see[i])
    q3=driver.find_element(By.XPATH,value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
    q3.send_keys(links_see[i])
    time.sleep(2)
    submit=driver.find_element(By.XPATH,value="//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div")
    submit.click()
    time.sleep(5)

