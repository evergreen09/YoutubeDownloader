from pytube import YouTube
import re
import csv



def uTubeDownload(Download, page):
    
    userName = re.findall('@([a-zA-Z0-9]+)', page)
    DOWN_DIRT = Download + '\\' + str(userName[0])
    csv_file = str(userName[0]) + '.csv'
    with open(csv_file) as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            url = str(row)
            yt = YouTube(url)
            stream = yt.streams.get_highest_resolution()
            stream.download(DOWN_DIRT)