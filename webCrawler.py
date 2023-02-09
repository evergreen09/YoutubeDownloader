import requests
import re
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import csv

linkcsv = 'links.csv'
linkarry = []
utube = 'https://www.youtube.com'


driver = webdriver.Chrome()
url = 'https://www.youtube.com/@PaniBottle/videos'

driver.get(url)


time.sleep(3)
content = driver.page_source.encode('utf-8').strip()
soup = BeautifulSoup(content,"html.parser")
firstVid = soup.findAll("a", {"id": "video-title-link"})
for link in firstVid:
    for utlink in link:
        linkarry.append([str(utube) + str(link.get('href'))])
with open(linkcsv, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(linkarry)
print(linkarry)


