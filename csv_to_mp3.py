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
from bs4 import BeautifulSoup

songs_csv = "songs.csv"

def get_href(url):
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, "lxml")
    # Get all the links to videos, because the first might be an ad
    tag = [a['href'] for a in soup.find_all("a", {'class', 'yt-uix-tile-link'}, text=True)]
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
	while i<len(songs["song"]):
		this_song = songs["song"][i]+" "+ songs["artist"][i]
		this_search = "+".join(this_song.strip().split())
		div = get_href(search_url+this_search)
		# sometimes the first is an ad and ads start with 'https...' whereas genuine video links are just the "/asDFeG4BLaH" 
		if "https" not in div[0]:
			link_ext = div[0]
		else:
			link_ext = div[1]
		complete_link = yt_link+link_ext
		print(i, this_song, complete_link)
		yt_dler(complete_link)
		i+=1

if __name__ == "__main__":
    main()