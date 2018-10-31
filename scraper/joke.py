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


id=1
for i in range(0,1901,20):
	s = "https://worstjokesever.com/short-jokes?skip="+str(i)
	browser.get(s)
	#time.sleep(2)
	ele = browser.find_elements_by_xpath("//section[@class='Article__content']/p")
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
		save_path_file = "joke.xml"
		with open(save_path_file,"w",encoding='utf8') as f:
			f.write(xml_str)

