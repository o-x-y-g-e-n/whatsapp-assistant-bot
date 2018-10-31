

import xml.etree.ElementTree as ET
import random
def fact_generator():
	x = random.randint(1,1001)
	tree = ET.parse('../datasets/fact.xml')
	root = tree.getroot()
	ele = root.findall(".//line[@id='"+(str(x))+"']/line-text")[0]
	return ele.text
