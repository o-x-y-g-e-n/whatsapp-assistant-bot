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

def calc_generator(stri):

	strl = stri[6:]
	browser = webdriver.Chrome("/home/oxygen_/Documents/chromedriver")
	s = "https://www.google.com"
	browser.get(s)

	time.sleep(1)
	sele = browser.find_element_by_id('lst-ib')
	sele.send_keys(str(strl))
	sele.send_keys(Keys.ENTER)
	time.sleep(2)

	myele = browser.find_element_by_id('cwos')
	ans = myele.text
	browser.quit()
	return ans