
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
from xml.dom import minidom
from tqdm import tqdm
import os

browser = webdriver.Chrome("/home/oxygen_/Documents/chromedriver")
root = minidom.Document()
xml = root.createElement('lines') #root
root.appendChild(xml)
s = "http://www.quotationspage.com/random.php3"
browser.get(s)

e1 = browser.find_elements_by_xpath("//input[@name='collection[]']")
for e in e1:
	if not (e.is_selected()):
		e.click()

id=1
for i in range(1,80):
	time.sleep(2)
	ele = browser.find_elements_by_xpath("//a[@title='Click for further information about this quotation']")
	for e in ele:
		lineschild = root.createElement('line')
		lineschild.setAttribute('id',str(id))
		xml.appendChild(lineschild)
		childofline = root.createElement('line-text')
		texti = e.text
		childofline.appendChild(root.createTextNode(texti))
		lineschild.appendChild(childofline)
		id=id+1	
		#creating XML file
		xml_str = root.toprettyxml(indent="\t")
		save_path_file = "quotes.xml"
		with open(save_path_file,"w",encoding='utf8') as f:
			f.write(xml_str)
	btn = browser.find_element_by_xpath("//input[@value='New Random Quotations']")
	btn.click();


