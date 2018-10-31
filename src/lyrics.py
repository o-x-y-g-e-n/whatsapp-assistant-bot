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

def lyrics_generator(stri):
	browser = webdriver.Chrome("/home/oxygen_/Documents/chromedriver")
	mystr = stri[8:]
	# print(mystr)
	s = "https://www.musixmatch.com/"
	browser.get(s)
	time.sleep(10)
	sbtn = browser.find_element_by_xpath('//*[@id="site"]/div/div[1]/div/main/div/div[1]/div[2]/div/div/div/div[1]/div/span/span/span/form/div/div[1]/input')
	sbtn.send_keys(str(mystr))
	time.sleep(8)
	mysearch = browser.find_element_by_xpath('//*[@id="site"]/div/div[1]/div/main/div/div[1]/div[2]/div/div/div/div[1]/div/span/span/span[2]/div/div/div/div[1]/div[2]/div/ul/li/a/div[2]/h2')
	mysearch.click()
	time.sleep(2)
	ele = browser.find_elements_by_class_name('mxm-lyrics__content ')
	strl = " "
	for e in ele:
		strl += e.text
	browser.quit()
	return strl		