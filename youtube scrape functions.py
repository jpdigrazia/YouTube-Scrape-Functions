
from pytube import YouTube
import subprocess
import os
import pandas as pd 

indat = pd.read_csv("combined_vidlist.csv") 
items = list(indat['url'])  #need to clean up input
ids = list(indat['id'])

#download location
vd_path="C:\\Users\\Joseph.DiGrazia\\OneDrive - 365shl\\YouTube Project\\video downloads"


def yscrape(items, vd_path, ids):
    c=0
    for i in items:
        print(i)
        n = str(ids[c]) +' - ' + i
        yt = YouTube(i)
        video=yt.streams.first()
        video.download(output_path=vd_path, filename=str(n))
        c = c+1
    return;

in_path="\\video downloads"
out_path="\\audio extractions"

def extract(in_path, out_path):
    files=os.listdir(in_path)
    for f in files:
      infp='\"'+in_path+f+'\"'
      outfp='\"'+out_path+f[:-3]+"wav"+'\"'
      command = "ffmpeg -i " +infp+" -ab 160k -ac 2 -ar 44100 -vn "+outfp 
      print(command)
      subprocess.call(command, shell=True)
    return;

yscrape(items[0:10], vd_path, ids)
extract(in_path, out_path)
