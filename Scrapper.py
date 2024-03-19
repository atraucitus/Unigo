from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import requests
from bs4 import BeautifulSoup
import time
import IPython

options = webdriver.ChromeOptions()
options.binary_location = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
chrome_driver_binary = r"C:/Users/Max/.wdm/chromedriver/75.0.3770.8/win32/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
name = []
approvedby = []
driver.implicitly_wait(30)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
page = requests.get('https://collegedunia.com/btech-colleges?city_id=125', headers=headers)
try:
    SCROLL_PAUSE_TIME = 0.5
    driver.get("https://collegedunia.com/btech-colleges?city_id=125")

    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
        soup = BeautifulSoup(page.text, 'html.parser')
        soup
        bage = soup.body
        tage = soup.title
        texts = bage.find_all('div', class_='jsx-18625286 clg-name-address')
        texts2 = bage.find('div', class_='jsx-2735629048 jsx-2684116272 jsx-3477660809 row listing-block-container')
        for text2 in texts2:
          card_base2 = text2.text
finally:
    driver.quit()
