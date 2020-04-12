import bs4

from selenium import webdriver

import sys
import time

import subprocess


def getWFSlot(productUrl):
   driver = webdriver.Chrome("D:\Program Files (x86)\Python\Lib\site-packages\chromedriver_binary\chromedriver.exe")
   driver.get(productUrl)           
   html = driver.page_source
   soup = bs4.BeautifulSoup(html)
   time.sleep(60)
   no_open_slots = True

   duration = 5000
   #milliseconds
   freq = 440


   while no_open_slots:
      driver.refresh()
      print("refreshed")
      html = driver.page_source
      soup = bs4.BeautifulSoup(html)
      time.sleep(4)

      slot_pattern = 'Next available'
      try:
         next_slot_text = soup.find('h4', class_ ='ufss-slotgroup-heading-text a-text-normal').text
         print("text: %s"%next_slot_text)
         if slot_pattern in next_slot_text:
            print('SLOTS OPEN!')
            subprocess.call(["afplay", "music.wav"])
            time.sleep(60000)
      except AttributeError:
         i = 0

      try:
         no_slot_pattern = 'No delivery windows available. New windows are released throughout the day.'
         no_slot_text = soup.find('h4', class_ ='a-alert-heading').text
         print("No slot: %s"%no_slot_text)
         if no_slot_pattern == no_slot_text:
            print("NO SLOTS!")
         else:
            subprocess.call(["afplay", "music.wav"])
      except AttributeError: 
         print('SLOTS OPEN!')
         subprocess.call(["afplay", "music.wav"])
         time.sleep(60000)


getWFSlot('https://www.amazon.com/gp/buy/shipoptionselect/handlers/display.html?hasWorkingJavascript=1')


