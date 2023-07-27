import os
from pytube import YouTube
import ffmpeg

def download_youtube_video(url, output_path):
    try:
        # Download the video using pytube
        yt = YouTube(url)
        video_stream = yt.streams.filter(only_audio=True).first()
        print(f"Downloading '{yt.title}' as MP3...")
        video_stream.download(output_path)

        # Get the downloaded video's file path
        video_filename = video_stream.default_filename
        video_file_path = os.path.join(output_path, video_filename)

        # Convert the downloaded video to MP3 using ffmpeg
        audio_output_filename = f"{yt.title}.mp3"
        audio_output_path = os.path.join(output_path, audio_output_filename)

        ffmpeg.input(video_file_path).output(audio_output_path, acodec='libmp3lame').run()

        # Remove the downloaded video file (optional)
        os.remove(video_file_path)

        print("Download and conversion completed successfully.")
        return audio_output_path

    except Exception as e:
        print("An error occurred:", str(e))
        return None

if __name__ == "__main__":
    youtube_url = input("Enter the YouTube video URL: ")
    output_directory = r'C:\Users\Campbell\Downloads'
    
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    mp3_file = download_youtube_video(youtube_url, output_directory)

    if mp3_file:
        print(f"MP3 saved to: {mp3_file}")
    else:
        print("Failed to download the YouTube video.")
