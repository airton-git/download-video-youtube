from pytubefix import YouTube
from pytubefix.cli import on_progress

#Recebe a URL do vídeo e faz o download.
url = "https://youtube.com/watch?v=f4k7mweehI4"

yt = YouTube(url, on_progress_callback=on_progress)
title = yt.title
#Algumas informações retornadas do vídeo.
print("="*60,"\n")
print("Url: ", url)
print("Título: ", title)
print("Author: ", yt.author)
print("Url do Canal: ", yt.channel_url)

# Faz o download do vídeo em alta resolução.
ys = yt.streams.get_highest_resolution()
ys.download(filename=title + ".mp4")

print("\nDownload concluído!", flush=True)
print("="*60,"\n")
