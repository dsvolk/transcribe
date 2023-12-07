import re

from yt_dlp import YoutubeDL


def is_youtube_link(link: str) -> bool:
    # Regular expression for matching YouTube URLs
    youtube_regex = (
        r"(https?://)?(www\.)?"
        r"(youtube|youtu|youtube-nocookie)\.(com|be)/"
        r"(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})"
    )

    match = re.match(youtube_regex, link)
    return bool(match)


def download_audio_from_youtube(url: str):
    videoinfo = YoutubeDL().extract_info(url=url, download=False)
    length = videoinfo["duration"]
    filename = f"./data/tmp/audio/youtube/{videoinfo['id']}.mp3"
    options = {
        "format": "bestaudio/best",
        "keepvideo": False,
        "outtmpl": filename,
    }
    with YoutubeDL(options) as ydl:
        ydl.download([videoinfo["webpage_url"]])
    return filename, length
