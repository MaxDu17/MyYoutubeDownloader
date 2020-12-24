# from pytube import YouTube
# a = input("link? \n")
# YouTube(a).streams.first().download(output_path = "G:/Desktop/Downloaded Vids")
import pytube

print("Give URL:")
url = input()

pytube.YouTube(url).streams.get_highest_resolution().download('Video')