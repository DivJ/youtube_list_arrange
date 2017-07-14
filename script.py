import urllib
import os
from bs4 import BeautifulSoup
url=""
path=""
data=urllib.urlopen(url).read()
soup=BeautifulSoup(data)
names=[]
for link in soup.find_all('a',attrs={'class':"pl-video-title-link yt-uix-tile-link yt-uix-sessionlink spf-link "}):
    names.append(link.contents)
names=[str(b.strip()) for a in names for b in a]
names=[a.replace('/','_')for a in names]
print names
video_names=[]
for video in os.listdir(path):
    video_names.append(video[:-4])
print video_names
for id in video_names:
    os.rename(path+"\\"+id+".mp4",path+"\\"+str(names.index(id)+1)+" "+id+".mp4")
