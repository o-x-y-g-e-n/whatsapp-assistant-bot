import xml.etree.ElementTree as ET
import random
def joke_generator():
	x = random.randint(1,2416)
	tree = ET.parse('../datasets/joke.xml')
	root = tree.getroot()
	ele = root.findall(".//line[@id='"+(str(x))+"']/line-text")[0]
	return ele.text
