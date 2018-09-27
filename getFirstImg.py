import os

import cv2

videos_src_path = 'D:/TBSI/2F/data/train_station_new/work/'
videos_save_path = 'D:/TBSI/2F/data/train_station_img_new/'

videos = os.listdir(videos_src_path)
videos = filter(lambda x: x.endswith('avi'), videos)

for each_video in videos:
    print(each_video)

    # get the name of each video, and make the directory to save frames
    each_video_name, _ = each_video.split('.')
    #os.mkdir(videos_save_path + '/' + each_video_name)

    #each_video_save_full_path = os.path.join(videos_save_path, each_video_name) + '/'

    # get the full path of each video, which will open the video tp extract frames
    each_video_full_path = os.path.join(videos_src_path, each_video)

    cap  = cv2.VideoCapture(each_video_full_path)
    frame_count = 0
    success = True
    success, frame = cap.read()
    #print('Read a new frame: ', success)
    cv2.imwrite(videos_save_path + each_video_name + "_%d.jpg " % frame_count, frame)

cap.release()