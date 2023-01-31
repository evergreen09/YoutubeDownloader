import requests
from selenium import webdriver
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
url = 'https://www.youtube.com/@PaniBottle/videos'
driver.maximize_window()
driver.get(url)


time.sleep(5)
content = driver.page_source.encode('utf-8').strip()
soup = BeautifulSoup(content,"html.parser")
firstVid = soup.findAll("a", {"id": "video-title-link"})

print(firstVid)
