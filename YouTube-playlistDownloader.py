import yt_dlp

def get_video_quality():
    # Ask user for preferred video quality
    print("Available Video Quality Options:")
    print("1. Best Quality (Highest resolution available)")
    print("2. 1080p (if available)")
    print("3. 720p (if available)")
    print("4. 480p (if available)")
    print("5. 360p (if available)")
    
    choice = input("Enter the number corresponding to your preferred video quality: ")

    if choice == '1':
        return 'bestvideo+bestaudio'
    elif choice == '2':
        return 'bestvideo[height<=1080]+bestaudio'
    elif choice == '3':
        return 'bestvideo[height<=720]+bestaudio'
    elif choice == '4':
        return 'bestvideo[height<=480]+bestaudio'
    elif choice == '5':
        return 'bestvideo[height<=360]+bestaudio'
    else:
        print("Invalid choice, defaulting to 720p.")
        return 'bestvideo[height<=720]+bestaudio'

def download_playlist():
    # Ask user for the playlist URL
    playlist_url = input("Enter the YouTube playlist URL: ")

    # Ask user for preferred video quality
    video_quality = get_video_quality()

    # Set up options for yt-dlp
    ydl_opts = {
        'format': video_quality,  # Video quality selected by user
        'outtmpl': '%(playlist)s/%(title)s.%(ext)s',  # Folder structure: Playlist name -> Video title
        'merge_output_format': 'mp4',  # Merges audio and video into mp4
        'noplaylist': False,  # Ensure playlist download is enabled
    }

    # Use yt-dlp to download the playlist
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print(f"Starting download for playlist: {playlist_url}")
        ydl.download([playlist_url])
        print("Download completed.")

if __name__ == "__main__":
    download_playlist()
