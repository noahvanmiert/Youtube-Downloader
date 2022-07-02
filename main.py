# Made by Noah Van Miert
# Project: Youtube Video Downloader

from pytube import YouTube

import sys
import time

def get_flags():
    if len(sys.argv) < 2:
        print("Error: no url was given.")
        exit(1)

    url = ""

    flags = {"title": False, "description": False, "views": False, "length": False}

    for argument in sys.argv:

        # check if argument is a flag
        if argument[0] == '-':
            argument = argument[1:]

            if argument == "title":
                flags['title'] = True

            elif argument == "description":
                flags['description'] = True
                
            elif argument == "views":
                flags['views'] = True

            elif argument == "length":
                flags['length'] = True
        else:
            url = argument
        
    return url, flags
    
def print_data_from_video(video, flags):

    if flags['title']: print(f"Title: {video.title}")
    if flags['description']: print(f"Description: {video.description}")
    if flags['views']: print (f"Views: {video.views}")
    if flags['length']: print (f"Lenght {video.length}")

video = YouTube(get_flags()[0])
print_data_from_video(video, get_flags()[1])

def download_video():
    print("Download: started (this can take a while)")
    high_resolution_video = video.streams.get_highest_resolution()
    start = time.time()
    high_resolution_video.download()
    print("Download: finished")
    print(f"Download took: {time.time() - start} seconds")

download_video()
