from pytube import YouTube


try:
    video = YouTube("https://www.youtube.com/watch?v=lEflo_sc82g")
    for stream in video.streams:
        print(stream)
except Exception as e:
    print(f"An error occurred: {e}")
