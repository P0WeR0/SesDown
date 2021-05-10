from youtube_dl import YoutubeDL
import time

audio_downloader = YoutubeDL({'format':'bestaudio'})


while 1:
    print('SesDown'.center(20, '-'))

    yt_raw = "https://www.youtube.com/watch?v="
    yt_id = input("Youtube id giriniz: ")

    url = yt_raw + yt_id

    audio_downloader.extract_info(url)

    tekrar = input("\nYeniden bir dosya indirmek istiyor musunuz?\ne/h? = ")

    if tekrar == "h":
        time.sleep(1)
        break