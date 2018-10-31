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

def youtube_generator(stri):
	browser = webdriver.Chrome("/home/oxygen_/Documents/chromedriver")
	strl = stri[8:]
	s = "https://www.google.com"
	browser.get(s)
	time.sleep(1)
	sele = browser.find_element_by_id('lst-ib')
	sele.send_keys(str(strl))
	sele.send_keys(Keys.ENTER)

	tab_change  = browser.find_element_by_xpath("//a[text()='Videos']")
	tab_change.click()

	stlink = browser.find_elements_by_xpath("//*[@class='r']/a")

	myele = stlink[0].get_attribute("href")
	browser.quit()
	return(myele)