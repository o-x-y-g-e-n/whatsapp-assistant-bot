
import xml.etree.ElementTree as ET
import random
def quote_generator():
	x = random.randint(1,1581)
	tree = ET.parse('../datasets/quotes.xml')
	root = tree.getroot()
	ele = root.findall(".//line[@id='"+(str(x))+"']/line-text")[0]
	return ele.text
