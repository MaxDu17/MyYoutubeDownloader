from pytube import YouTube
a = input("link? \n")
YouTube(a).streams.first().download(output_path = 'C:/Users/wedu/Desktop/Downloaded Vids')
