from webCrawler import *
from utubeDown import *
import re

print('Welcome to UTube Downloader!')

page = input('Enter the url of the Youtube page: ')
urlCheck = re.findall('videos$', page)

if urlCheck:
    utubelink(page)
else:
    print('Invalid URL')

onoff = input('Would you like to download videos? : (T|F)')

if onoff == 'T' or onoff == 't':
    Download = input('Choose download directory: ')
    uTubeDownload(Download)
elif onoff == 'F' or onoff == 'f':
    print('Program Exit')
else:
    print('Program Exit')