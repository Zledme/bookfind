
from bs4 import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.firefox.service import Service 
from selenium.webdriver.common.by import By
import time
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as w


def setup(driver_path):
   ser = Service(driver_path)
   op = webdriver.FirefoxOptions()
   driver = webdriver.Firefox(service=ser, options=op)
   return driver 

def getting_page(typeofbook,n):
   driver = setup("./geckodriver")
   driver.get('https://www.goodreads.com/shelf/show/'+typeofbook)
   for i in range(1,n):
      driver.execute_script("window.scrollTo(1,50000)")
      time.sleep(5)
   pagesource = driver.page_source
   driver.close()
   soup = BeautifulSoup(pagesource,'html.parser')
   elements = soup.find_all ("a", class_="bookTitle")
   titles = [element.text for element in elements]
   print(titles)

getting_page(input("type of book:"),int(input('No of times you want to scroll : ')))
