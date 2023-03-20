#https://github.com/duvu/pytube/pull/1
#pip3 install ffmpeg moviepy pydub


import pytube, sys, moviepy.editor as mp
from imageio.core import Dict
from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    #youtubeObject = youtubeObject.streams.get_audio_only()
    try:
        print("start...")
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")


link = input("Enter the YouTube video URL: ")
#if link ==== string.empty:

#link = "https://www.youtube.com/watch?v=ro4gO93dJok"
#Download(link)
#Download("https://www.youtube.com/watch?v=ro4gO93dJok")
#print("done")
my_clip = mp.VideoFileClip(r"ВЛАДИМИР ВОЙНОВИЧ «МОСКВА 2042 Часть 1» Аудиокнига Читает Всеволод Кузнецов.mp4")
print ("extract mp3")
my_clip.audio.write_audiofile(r"ВЛАДИМИР ВОЙНОВИЧ «МОСКВА 2042 Часть 1» Аудиокнига Читает Всеволод Кузнецов.mp3")
