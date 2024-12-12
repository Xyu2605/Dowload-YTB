import yt_dlp
import os
import urllib.parse

def download_mp4(url):
    youtube_url = url
    global downloaded_file_name
    downloaded_file_name = "unknown.mp4"  # Default file name

    # Ensure the static directory exists

    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',  # Download best video and audio combined
        'outtmpl': f'%(title)s.%(ext)s',  # Save video with title as filename
        'noplaylist': True,  # Do not download playlists
        'nocheckcertificate': True,  # Ignore certificate verification issues
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

    # Encode file name for URLdsd
    encoded_file_name = urllib.parse.quote(downloaded_file_name)
    
    # Return the file path for download
    file_path = downloaded_file_name[:-4] + "mp4"
    print(file_path)

    if file_path and os.path.exists(file_path):
        return {"file_name": file_path}
    else:
        return {"error": "Failed to download file"}

link = input("Enter your URL > ")
download_mp4(link)