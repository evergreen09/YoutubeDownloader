import requests
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import csv

def utubelink(page):
    driver = webdriver.Chrome()
    linkcsv = 'links.csv'
    linkarry = []
    utube = 'https://www.youtube.com'
    
    def scrollDown():
        i = 5000
        for x in range(10):
            driver.execute_script("window.scrollTo("+ str(i - 5000) +"," + str(i) + ")")
            i += 5000
            time.sleep(1)

    url = str(page)
    driver.get(url)
    time.sleep(1)
    scrollDown()

    content = driver.page_source.encode('utf-8').strip()
    soup = BeautifulSoup(content,"html.parser")
    firstVid = soup.findAll("a", {"id": "video-title-link"})

    for link in firstVid:
        for utlink in link:
            linkarry.append([str(utube) + str(link.get('href'))])
    with open(linkcsv, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(linkarry)
