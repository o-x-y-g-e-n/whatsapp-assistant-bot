
import xml.etree.ElementTree as ET
import random

def flirt_generator():
	x = random.randint(1,1110)
	tree = ET.parse('../datasets/flirt.xml')
	root = tree.getroot()
	ele = root.findall(".//line[@id='"+(str(x))+"']/line-text")[0]
	return ele.text
