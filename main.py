## YOUTUBE DOWNLOADER WITH PYTHON

# import regex
import re
# import pytube
from pytube import YouTube

# get link from user
link = input("Please Enter YouTube Video Link : ")
yt = YouTube(link)

# get all streams
videos = yt.streams
video = list(enumerate(videos))

# showing reasult in table
print("+","="*4,"+","="*12,"+","="*12,"+",sep="")
print("|","ID","|","  FORMAT  ","|","RESOLUTION","|") 
print("+","="*4,"+","="*12,"+","="*12,"+",sep="")

# print id, format & resolution
for i in video :
    i = str(i)
    s = re.findall("([0-9]{1,2}).+?mime_type=(\".+?\") ...=(\".+?\")",i)
    for item in s :
        print ("|",item[0].center(2),"|",item[1].replace('"','').center(10),"|",item[2].replace('"','').center(10),"|")
print("+","="*4,"+","="*12,"+","="*12,"+",sep="")

# ask from user to select id to download
x = int(input("Enter ID to Download : "))
print("Downloaing ..")

# download video
dn = videos[x]
dn.download()

print("Downloaded Successfully") 

#value = video.streams.get_by_itag(133)
#print(value.filesize_approx)