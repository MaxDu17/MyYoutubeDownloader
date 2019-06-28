from pytube import YouTube
a = input("link? \n")

yt = YouTube(a)
vids = yt.streams.all()
print(vids)
#YouTube(a).streams.first().download("C:/Users/wedu/Desktop/Downloaded Vids")