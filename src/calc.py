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
from configparser import SafeConfigParser
import os.path
from util import get_config_information
def calc_generator(stri):
	browser = webdriver.Chrome(str(get_config_information()))
	s = "https://www.google.com"
	browser.get(s)
	
	strl = stri[6:]
	time.sleep(1)
	sele = browser.find_element_by_id('lst-ib')
	sele.send_keys(str(strl))
	sele.send_keys(Keys.ENTER)
	time.sleep(2)

	myele = browser.find_element_by_id('cwos')
	ans = myele.text
	browser.quit()
	return ans