import youtube_dl
import os

# video_ids = ['dQw4w9WgXcQ', '9bZkp7q19f0', '2Vv-BfVoq4g', 'KQ6zr6kCPj8', 'X2WH8mHJnhM']
video_ids =["dQw4w9WgXcQ"]
# Create a folder to save the downloaded videos
if not os.path.exists("downloads"):
    os.makedirs("downloads")

# Set the YouTube-dl options
# ydl_opts = {
#     'format': 'bestvideo[ext=webm][height=144]+bestaudio[ext=webm]/best[height=144]',
#     'outtmpl': 'downloads/%(title)s.%(ext)s',
#     'prefer_ffmpeg': True
# }
ydl_opts = {
    'format': 'bestvideo[ext=webm][height=144]+bestaudio[ext=webm]/best[height=144]',
    'verbose': True,
    'prefer_ffmpeg': True,
    'outtmpl': 'downloads/%(title)s.%(ext)s',
    'prefer_ffmpeg': True
}


with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    for video_id in video_ids:
        ydl.download(['https://www.youtube.com/watch?v=' + video_id])
