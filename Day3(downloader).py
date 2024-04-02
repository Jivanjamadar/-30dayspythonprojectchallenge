from pytube import YouTube
from pytube import Playlist

print("-------Downloader for Videos or Playlist form YouTube------")


pref=int(input("""What do you wanna to download \n 1)Audio  2)Video  3)Playlist  \n (Plaease , enter the number)\n""") )

if pref==1:
    link=input("Please , enter the URL :")
    youtube_1=YouTube(link)
    print(youtube_1.title)
    videos=youtube_1.streams.filter(only_audio=True)
    vid=list(enumerate(videos))
    for i in vid:
     print(i)
    print()
    strm=int(input("Please , enter your preference :"))
    videos[strm].download() 
    print("Successfully download !")
elif pref==2:
    link=input("Please , enter the URL :")
    youtube_1=YouTube(link)
    print(youtube_1.title)
    videos=youtube_1.streams.filter(only_video=True)
    vid=list(enumerate(videos))
    for i in vid:
     print(i)
    print()
    strm=int(input("Please , enter your preference :"))
    videos[strm].download() 
    print("Successfully download !")

elif pref==3:
     link=input("Please , enter the URL :")
     py = Playlist(link)
     print(f'Downloading : {py.title}')
     for video in py.videos:
        video.streams.first().download()





