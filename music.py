import yt_dlp

ydl_opts = {
    'format': 'bestaudio/best',
    'ffmpeg_location': r'C:\ffmpeg\bin',
    'postprocessors': [
        {
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }
    ],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
  ydl.download(['https://www.youtube.com/watch?v=R2s4jKfEVnA'])

#ffmpeg
# justpaste.it/iq3it
# windows
# winget install --id Gyan.FFmpeg -e
# 'ffmpeg_location': r'C:\ffmpeg\bin',