import bs4

from selenium import webdriver

import sys
import time

import winsound


def getWFSlot(productUrl):
   driver = webdriver.Chrome("D:\Program Files (x86)\Python\Lib\site-packages\chromedriver_binary\chromedriver.exe")
   driver.get(productUrl)           
   html = driver.page_source
   soup = bs4.BeautifulSoup(html)
   time.sleep(60)
   no_open_slots = True

   #milliseconds
   duration = 5000
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
            print('1: SLOTS OPEN!')
            winsound.Beep(freq, duration)
            winsound.Beep(freq, duration)
            winsound.Beep(freq, duration)
            winsound.Beep(freq, duration)
            winsound.Beep(freq, duration)
            time.sleep(120)
      except AttributeError:
         print('1: find failed')

      try:
         no_slot_pattern = 'No delivery windows available. New windows are released throughout the day.'
         no_slot_warning = 'Due to increased demand'
         no_slot_text = soup.find('h4', class_ ='a-alert-heading').text
         print("No slot: %s"%no_slot_text)
         if no_slot_pattern in no_slot_text:
            print("NO SLOTS!")
         elif no_slot_warning in no_slot_text:
            print("NO SLOT WARNING!")
         else:
            print("2: SLOT OPEN!")    
            winsound.Beep(freq, duration)
            winsound.Beep(freq, duration)
            winsound.Beep(freq, duration)
            winsound.Beep(freq, duration)
            winsound.Beep(freq, duration)
            time.sleep(120)
      except AttributeError: 
         print('2: find failed! SLOTS MAY OPEN!')
         winsound.Beep(freq, duration)
         winsound.Beep(freq, duration)
         winsound.Beep(freq, duration)
         winsound.Beep(freq, duration)
         winsound.Beep(freq, duration)
         time.sleep(120)


getWFSlot('https://www.amazon.com/gp/buy/shipoptionselect/handlers/display.html?hasWorkingJavascript=1')


