from yt_dlp import YoutubeDL


def download_audio_from_url(url):
    videoinfo = YoutubeDL().extract_info(url=url, download=False)
    length = videoinfo["duration"]
    filename = f"./audio/youtube/{videoinfo['id']}.mp3"
    options = {
        "format": "bestaudio/best",
        "keepvideo": False,
        "outtmpl": filename,
    }
    with YoutubeDL(options) as ydl:
        ydl.download([videoinfo["webpage_url"]])
    return filename, length
