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

def define_generator(stri):
	browser = webdriver.Chrome("/home/oxygen_/Documents/chromedriver")
	strl = stri[8:]
	s = "https://www.google.com"
	browser.get(s)
	time.sleep(1)
	sele = browser.find_element_by_id('lst-ib')
	sele.send_keys("define " + str(strl))
	sele.send_keys(Keys.ENTER)
	time.sleep(2)
	strr = " "
	sres = browser.find_elements_by_xpath("//*[@data-dobid='dfn']/span")
	for s in sres:
		strr += s.text
	browser.quit()
	return(strr)