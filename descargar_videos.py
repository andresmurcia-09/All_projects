import yt_dlp as youtube_dl

def descargar_video(url):
    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s',
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

url = input("Ingrese la URL del video a descargar: ")
descargar_video(url)
