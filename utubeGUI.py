import tkinter as tk
import re
from webCrawler import *
from utubeDown import *

def run_downloader():
    page = entry_url.get()
    urlCheck = re.findall('videos$', page)

    if urlCheck:
        utubelink(page)
    else:
        result_label.config(text='Invalid URL')
        return
    
    onoff = entry_onoff.get()

    if onoff == 'T' or onoff == 't':
        Download = entry_dir.get()
        uTubeDownload(Download, page)
        result_label.config(text='Download Complete!')
    elif onoff == 'F' or onoff == 'f':
        result_label.config(text='Program Exit')
    else:
        result_label.config(text='Program Exit')

root = tk.Tk()
root.title("U-Tube Downloader")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

url_label = tk.Label(frame, text="Enter the URL of the Youtube page:")
url_label.grid(row=0, column=0, pady=5)

entry_url = tk.Entry(frame)
entry_url.grid(row=0, column=1, pady=5)

onoff_label = tk.Label(frame, text="Would you like to download videos? (T|F)")
onoff_label.grid(row=1, column=0, pady=5)

entry_onoff = tk.Entry(frame)
entry_onoff.grid(row=1, column=1, pady=5)

dir_label = tk.Label(frame, text="Choose download directory:")
dir_label.grid(row=2, column=0, pady=5)

entry_dir = tk.Entry(frame)
entry_dir.grid(row=2, column=1, pady=5)

result_label = tk.Label(frame)
result_label.grid(row=3, column=0, columnspan=2, pady=5)

download_button = tk.Button(frame, text="Download", command=run_downloader)
download_button.grid(row=4, column=0, columnspan=2, pady=5)

root.mainloop()
