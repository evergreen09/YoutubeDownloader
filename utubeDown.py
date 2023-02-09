from pytube import YouTube
import csv



def uTubeDownload(Download):
    DOWN_DIRT = Download
    with open('links.csv') as file_obj:
        reader_obj = csv.reader(file_obj)
        for row in reader_obj:
            url = str(row)
            yt = YouTube(url)
            stream = yt.streams.get_highest_resolution()
            stream.download(DOWN_DIRT)