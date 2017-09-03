# csv to mp3 #

### Description: ###

This simple script takes a .csv list of popular song titles and artist names
and searches youtube for that song, grabs the first link that isn't an ad and
downloads the video and converts it to mp3 using youtube-dl/ffmpeg.

So you can listen to these songs off the [internet] grid!

*Not to be used to download music illegally!*
*Please follow local copyright law & support artists!!*

### Why: ###
Sometimes you don't have an internet connection and this is is an easy & lazy
way to download a couple of offline songs w/o worrying about torrenting
individual songs or using youtube2mp3 for each individual song.

Not recommended for building a large library - made for getting a few songs to
drag to my watch and dumb phone so I can listen to a couple new songs while out

### *Instructions:* ###

0. Clone this repo:
```
$ git clone https://github.com/HarryMaher/csv_to_mp3.git
```
1. Install ffmpeg (https://github.com/adaptlearning/adapt_authoring/wiki/Installing-FFmpeg)
2. Install youtube_dl, pandas, and bs4 with "pip3 install packagename"
3. Create a songs.csv in the same directory as this auto_yt_dl with a "song" and "artist" field
   (see current songs.csv for example of what it should look like)
4. Run this "python csv_to_mp3.py" (may take about a minute per song)
5. Drag the music to your offline device, and enjoy!

Note: It really only works for fairly popular songs that are on youtube...
