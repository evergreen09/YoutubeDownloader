from pytube import YouTube
import csv

DOWN_DIRT = r'C:\Users\j3642\Documents\utubedown'

with open('links.csv') as file_obj:
    reader_obj = csv.reader(file_obj)
    for row in reader_obj:
        url = str(row)
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download(DOWN_DIRT)