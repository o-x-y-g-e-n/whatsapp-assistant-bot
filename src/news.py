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


def news_generator(stri):
	browser = webdriver.Chrome("/home/oxygen_/Documents/chromedriver")
	s = "https://news.google.com"
	elem = []
	browser.get(s)
	if(len(stri) == 5):
		ele = browser.find_elements_by_xpath("//a[@role='heading'][@aria-level='2']")
		for e in ele:
		 	if(len(e.text) !=0):
		 		elem.append(e.text)	
		browser.quit()
		return elem	
		
	elif(str(stri[6:]) == 'technology'):
		btntech = browser.find_element_by_xpath("//a[text()='Technology']")
		btntech.click()
		time.sleep(3)
		ele = browser.find_elements_by_xpath("//a[@role='heading'][@aria-level='2']")
		for e in ele:
		 	if(len(e.text) !=0):
		 		elem.append(e.text)	
		browser.quit()
		return elem	
		
	elif(str(stri[6:]) == 'world'):
		btntech = browser.find_element_by_xpath("//a[text()='World']")
		btntech.click()
		time.sleep(3)
		ele = browser.find_elements_by_xpath("//a[@role='heading'][@aria-level='2']")
		for e in ele:
		 	if(len(e.text) !=0):
		 		elem.append(e.text)	
		browser.quit()
		return elem	
			
	elif(str(stri[6:]) == 'business'):
		btntech = browser.find_element_by_xpath("//a[text()='Business']")
		btntech.click()
		time.sleep(3)
		ele = browser.find_elements_by_xpath("//a[@role='heading'][@aria-level='2']")
		for e in ele:
		 	if(len(e.text) !=0):
		 		elem.append(e.text)	
		browser.quit()
		return elem	
			
	elif(str(stri[6:]) == 'entertainment'):
		btntech = browser.find_element_by_xpath("//a[text()='World']")
		btntech.click()
		time.sleep(3)
		ele = browser.find_elements_by_xpath("//a[@role='Entertainment'][@aria-level='2']")
		for e in ele:
		 	if(len(e.text) !=0):
		 		elem.append(e.text)	
		browser.quit()
		return elem	
			
	elif(str(stri[6:]) == 'sports'):
		btntech = browser.find_element_by_xpath("//a[text()='Sports']")
		btntech.click()
		time.sleep(3)
		ele = browser.find_elements_by_xpath("//a[@role='heading'][@aria-level='2']")
		for e in ele:
		 	if(len(e.text) !=0):
		 		elem.append(e.text)	
		browser.quit()
		return elem	
			
	elif(str(stri[6:]) == 'science'):
		btntech = browser.find_element_by_xpath("//a[text()='Science']")
		btntech.click()
		time.sleep(3)
		ele = browser.find_elements_by_xpath("//a[@role='heading'][@aria-level='2']")
		for e in ele:
		 	if(len(e.text) !=0):
		 		elem.append(e.text)	
		browser.quit()
		return elem	
			
	elif(str(stri[6:]) == 'health'):
		btntech = browser.find_element_by_xpath("//a[text()='Health']")
		btntech.click()
		time.sleep(3)
		ele = browser.find_elements_by_xpath("//a[@role='heading'][@aria-level='2']")
		for e in ele:
		 	if(len(e.text) !=0):
		 		elem.append(e.text)	
		browser.quit()
		return elem	
		
	elif(str(stri[6:]) == 'local'):
		btntech = browser.find_element_by_xpath("//div[text()='Local']")
		btntech.click()
		time.sleep(3)
		ele = browser.find_elements_by_xpath("//a[@role='heading'][@aria-level='2']")
		for e in ele:
		 	if(len(e.text) !=0):
		 		elem.append(e.text)	
		browser.quit()
		return elem	
		