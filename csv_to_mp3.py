#!/usr/bin/env python3

'''
# csv to mp3 #

### What it does: ###

This simple script takes a .csv list of popular song titles and artist names
and searches youtube for that song, grabs the first link that isn't an ad and
downloads the video and converts it to mp3 using youtube-dl/ffmpeg.

So you can listen to these songs off the [internet] grid!

### Why: ###
Sometimes you don't have an internet connection and this is is an easy & lazy
way to download a couple of offline songs w/o worrying about torrenting
individual songs or using youtube2mp3 for each individual song.

Not recommended for building a large library - intended for getting a few songs to
drag to my watch and dumb phone so I can listen to a couple new songs while out

*Not to be used to download music illegally!*
*Please follow local copyright law & support artists!!*



### *Instructions:* ###
1. Install ffmpeg (https://github.com/adaptlearning/adapt_authoring/wiki/Installing-FFmpeg)
2. Install youtube_dl, pandas, and bs4 with "pip3 install packagename"
3. Create a songs.csv in the same directory as this auto_yt_dl with a "song" and "artist" field
   (see current songs.csv for example of what it should look like)
4. Run this "python csv_to_mp3.py" (may take about a minute per song)
5. Drag the music to your offline device, and enjoy!

Note: It really only works for fairly popular songs that are on youtube.


todo:
- figure out how to get a csv output from spotify
- maybe worry about output song names?
- make into .exe?

credit:
https://stackoverflow.com/questions/30825371/extract-audio-equivalent-for-youtubedl-class

requires:
ffmpeg - google how to install it and put it in the same directory as your
all below modules (youtube_dl, pandas, bs4) - install w/ "pip3 install youtube_dl" and etc.

'''
import youtube_dl
import pandas as pd
import requests
#from bs4 import BeautifulSoup

songs_csv = "songs.csv"



def get_href(url):
    response = requests.get(url)
    content = response.content.__str__()
    # implemented without soup to make it working in 2023 , the below code searches the first youtube search url of 12 characters  in to the content string
    #soup = BeautifulSoup(content, "lxml")
    # Get all the links to videos, because the first might be an ad
    #tag = [a['href'] for a in soup.find_all("a", {'class', 'yt-uix-tile-link'}, text=True)]

    # Get the link to first video
    start = content.find('"/watch?v=') + 9
    end = start + 12
    tag: str = '/watch?v' + content[start:end]
    return tag


def yt_dler(vid_link):
    # d/l settings
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': True,
        'restrictfilenames': True}
    ydl = youtube_dl.YoutubeDL(ydl_opts)
    ydl.download([vid_link])


def main():
    songs = pd.read_csv(songs_csv)
    search_url = 'https://www.youtube.com/results?search_query='
    yt_link = 'http://www.youtube.com'
    i=0
    exception: str = ''

    while i<len(songs["song"]):
        this_song = songs["song"][i]+" "+ songs["artist"][i]
        this_search = "+".join(this_song.strip().split())
        div = get_href(search_url+this_search)
        # sometimes the first is an ad and ads start with 'https...' whereas genuine video links are just the "/asDFeG4BLaH"
        #if "https" not in div[0]:
            #link_ext = div[0]
        #else:
            #link_ext = div[1]
        # div would have desired url as returned by get_href , so above 4 lines are commented
        complete_link = yt_link+div
        print(i, this_song, complete_link)
        # exception handling such as age restricted video would not download and  to avoid interruption exception handling
        try :
            yt_dler(complete_link)
        except:
            exception = exception + complete_link + "\n"
        i+=1
    # Write the url of video which was not automatically downloaded with script to output.txt
    print(exception, file=open('output.txt', 'w'))
if __name__ == "__main__":
    main()