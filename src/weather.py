import re
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from xml.dom import minidom
from tqdm import tqdm
import datetime
from datetime import datetime


def weather_generator(stri):
	browser = webdriver.Chrome("/home/oxygen_/Documents/chromedriver")
	strl = stri[9:]
	s = "https://www.google.com"
	browser.get(s)
	time.sleep(1)
	sele = browser.find_element_by_id('lst-ib')
	sele.send_keys("weather " + str(strl))
	sele.send_keys(Keys.ENTER)
	time.sleep(2)	
	strr = " "

	myele = browser.find_element_by_id('wob_tm')
	mystring = str(myele.text)+" ℃"
	browser.quit()
	return mystring