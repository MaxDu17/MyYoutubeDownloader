from pytube import Playlist

a = input("link? \n")
pl = Playlist(a)
pl.download_all("C:/Users/Max Du/Downloads/yt downloads/playlists")