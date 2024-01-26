from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
cache_dr = "path/to/cache"
screen_size = "1920,1080"
options = Options()
options.headless = True
profile = webdriver.FirefoxProfile("/home/USERNAME/snap/firefox/common/.mozilla/firefox/A_HASH.default")
## path to your firefox profile
driver = webdriver.Firefox(options=options, firefox_profile=profile)
driver.set_window_size(1920, 1080)

print("Firefox Headless Browser Invoked")
driver.get("https://poe.com/ChatGPT")


chatbox_xpath = "/html/body/div[1]/div[1]/div/div/main/div/div/div/footer/div/div/div/textarea"


result_xpath = "/html/body/div[1]/div[1]/div/div/main/div/div/div/div[2]/div[3]"
result_div_class_substring = "ChatMessagesView_messagePair"

import warnings
import time
import os
from tqdm import trange

def start_chat():
    driver.get("https://poe.com/ChatGPT")
    while True:
        # ignore warning
        warnings.filterwarnings("ignore")
        input_text = input("input:")
        if input_text == "exit":
            break

        driver.find_element_by_xpath(chatbox_xpath).send_keys(input_text)
        driver.find_element_by_xpath(chatbox_xpath).send_keys(Keys.ENTER)

        driver.save_screenshot(os.path.join(cache_dr, "test.png"))

        for i in trange(20):
            time.sleep(1)
        
        driver.save_screenshot(os.path.join(cache_dr, "test2.png"))
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        result = soup.find_all(class_=re.compile(f".*{result_div_class_substring}.*"))
        result = [i.text for i in result]


        for i in result:
            print(i)
            print("===========")
try:
    start_chat()
except KeyboardInterrupt:




    driver.close()

