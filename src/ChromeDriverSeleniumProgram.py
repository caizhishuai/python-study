# encoding:utf-8
from selenium import webdriver
import os
import time

chromedriver = "D:/python3.5.3/Python35/chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver)
url='https://www.autohome.com.cn/all/'
browser.get(url)
print(browser.find_element_by_id('auto-channel-lazyload-article').text)
