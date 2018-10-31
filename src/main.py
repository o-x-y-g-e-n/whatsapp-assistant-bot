
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
import fact
import quote
import joke
import flirt
import os
import xml.etree.ElementTree as ET
import random
import mytime
import lyrics
import definine
import weather
import youtubee
import news
import calc
browser = webdriver.Chrome("/home/oxygen_/Documents/chromedriver")

s = "https://web.whatsapp.com/"
browser.get(s)


time.sleep(5)

browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[3]/label/input').click()


time.sleep(15)

commands = ["/quote","/funfact","/time","/joke","/calc","/conv","/lyrics","/define","/news","/weather","/wikipedia"]

browser.find_element_by_xpath('//div[@class="_25Ooe"]/span[@title="BOT"]').click()

time.sleep(7)
print("loop")
while True:
	lst_cmd = browser.find_elements_by_xpath('//div[@class="_3zb-j ZhF0n"]/span[last()]')
	lst_cmd_text = lst_cmd[-1].text
	lst_timer = browser.find_elements_by_xpath('//span[@class="_3EFt_"][last()]')
	lst_time = lst_timer[-1].text
	ssstr = datetime.now().strftime('%I:%M')
	print(lst_time)
	if(ssstr[0] == str('0')):
		system_hr =ssstr[1:2]
	else:
		system_hr = ssstr[0:2]
	system_min = ssstr[3:5]
	if(len(lst_time) == 7):
		wht_hr = lst_time[0:1]
	else:
		wht_hr = lst_time[0:2]
	wht_min = lst_time[2:4]
	print(str(system_hr) + " " + str(system_min))
	print()
	print(str(wht_hr)+ " " +str(wht_min))
	if(system_hr == wht_hr and system_min == wht_min):
	# print(lst_cmd_text)
		if(lst_cmd_text == '/quote'):
			print("quote here\n")
			ele = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]')
			tez = quote.quote_generator()
			ele.send_keys(str(tez))
			btn = browser.find_element_by_class_name("_2lkdt")
			btn.click()
		elif(lst_cmd_text == '/fact'):
			print("fact here\n")
			ele = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]')
			tez = fact.fact_generator()
			ele.send_keys(str(tez))
			btn = browser.find_element_by_class_name("_2lkdt")
			btn.click()
		elif(lst_cmd_text == '/flirt'):
			print("flirt here\n")
			ele = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]')
			tez = flirt.flirt_generator()
			ele.send_keys(str(tez))
			btn = browser.find_element_by_class_name("_2lkdt")
			btn.click()		
		elif(lst_cmd_text == '/joke'):
			print("joke here\n")
			ele = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]')
			tez = joke.joke_generator()
			ele.send_keys(str(tez))
			btn = browser.find_element_by_class_name("_2lkdt")
			btn.click()
		elif(lst_cmd_text == '/time'):
			print("time here\n")
			ele = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]')
			tez = mytime.time_generator()
			ele.send_keys(str(tez))
			btn = browser.find_element_by_class_name("_2lkdt")
			btn.click()
		elif(str(lst_cmd_text[0:7]) == "/lyrics"):
			print("lyrics here\n")
			ele = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]')
			tez = lyrics.lyrics_generator(str(lst_cmd_text))
			ele.send_keys(tez)
			btn = browser.find_element_by_class_name("_2lkdt")
			btn.click()
		elif(str(lst_cmd_text[0:7]) == "/define"):
			print("define here\n")
			ele = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]')
			tez = definine.define_generator(str(lst_cmd_text))
			ele.send_keys(tez)
			btn = browser.find_element_by_class_name("_2lkdt")
			btn.click()
		elif(str(lst_cmd_text[0:8]) == "/weather"):
			print("weather here\n")
			ele = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]')
			tez = weather.weather_generator(str(lst_cmd_text))
			ele.send_keys(tez)
			btn = browser.find_element_by_class_name("_2lkdt")
			btn.click()
		elif(str(lst_cmd_text[0:8]) == "/youtube"):
			print("youtbe here\n")
			ele = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]')
			tez = youtubee.youtube_generator(str(lst_cmd_text))
			ele.send_keys(tez)
			time.sleep(12)
			btn = browser.find_element_by_class_name("_2lkdt")
			btn.click()
		elif(str(lst_cmd_text[0:5]) == '/news'):
			print("news here\n")
			ele = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]')
			tez = news.news_generator(str(lst_cmd_text))
			for t in tez:
				ele.send_keys(t)
				btn = browser.find_element_by_class_name("_2lkdt")
				btn.click()
		elif(str(lst_cmd_text[0:5]) == "/calc"):
			print("calc here\n")
			ele = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]')
			tez =calc.calc_generator(str(lst_cmd_text))
			ele.send_keys(tez)
			btn = browser.find_element_by_class_name("_2lkdt")
			btn.click()
time.sleep(1000000)
