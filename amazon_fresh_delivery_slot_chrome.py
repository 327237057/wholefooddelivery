import bs4

from selenium import webdriver

import sys
import time
import os


AMAZON_FRESH_CART_URL = "https://www.amazon.com/gp/buy/shipoptionselect/handlers/display.html?hasWorkingJavascript=1"


def getWFSlot(productUrl):
    print("Start checking Amazon Fresh slots")
    # You need to set 'executable_path' to the path of the webdriver
    driver = webdriver.Chrome(
        executable_path="/Users/sitengjin/Documents/github/painjst/wholefooddelivery/chromedriver")
    driver.get(productUrl)
    html = driver.page_source
    soup = bs4.BeautifulSoup(html)
    # You 60 seconds to sign in on the pop-up amazon page to view your cart
    time.sleep(60)
    refresh_count = 0

    while True:
        driver.refresh()
        refresh_count += 1
        print(f"Page refreshed, total refresh count = {refresh_count}")
        html = driver.page_source
        soup = bs4.BeautifulSoup(html)
        time.sleep(2)

        try:
            open_slots = soup.find('div', class_='orderSlotExists').text()
            if open_slots != "false":
                print('SLOTS OPEN!')
                os.system('say "Slots for delivery opened!"')
                # You have 2 minutes to place your order, be quick!
                time.sleep(120)

        except AttributeError:
            # There is no open slots, continue
            continue
    
    return 0


if __name__ == "__main__":
    sys.exit(getWFSlot(AMAZON_FRESH_CART_URL))
