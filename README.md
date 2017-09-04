# csv to mp3 #

### *Description:* ###

This script takes a .csv file that contains a list of song titles and artist 
names, searches youtube for those songs, grabs links to the songs, and 
downloads videos and converts them to mp3 format.

Allows you to listen to these songs when you don't have internet!

*Not to be used to download music illegally!*
*Please follow local copyright law & support artists*

### *Why:* ###
Sometimes you don't have an internet connection and this is is an easy & lazy
way to download a couple of songs w/o worrying about looking for torrents for
individual songs or tediously going through a list of songs w/ youtube2mp3.

Not recommended for building a large library--made for getting ~5-15 new songs
to drag to an mp3 player to before going on a run or bike ride

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

Note: It really only works for decently popular songs on youtube