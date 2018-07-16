from pytube import YouTube
a = input("link? \n")

YouTube(a).streams.first().download("C:/Users/Max Du/Downloads/yt downloads")