from pytube import YouTube 

class Ytd:
    # where to save 
    SAVE_PATH = "./tempDownloads" #to_do 
    
    # link of the video to be downloaded 
    link = "https://youtu.be/2lAe1cqCOXo"

    try: 
        # object creation using YouTube 
        yt = YouTube(link) 
    except: 
        #to handle exception 
        print("Connection Error") 

    # Get the title of the video
    video_title = yt.title

    # Get all streams and filter for mp4 files
    mp4_streams = yt.streams.filter(file_extension='mp4')

    # get the video with the highest resolution
    # replacing nonetypes with 0
    res_list = [int(element.resolution[:-1]) if element.resolution is not None else 0 for element in mp4_streams]

    d_video = mp4_streams[res_list.index(max(res_list))]

    try: 
        # downloading the video 
        print(video_title)
        d_video.download(output_path=SAVE_PATH)
        print('Video downloaded successfully!')
    except: 
        print("Some Error!")
