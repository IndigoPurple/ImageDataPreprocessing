import os
import cv2

src_path = 'D:/TBSI/2F/data/66-nanshanPark/img/01/'
save_path = 'D:/WorkPlace/ano_pred_cvpr2018/Data/zhiyuan/testing/frames/01/'

#sequence = [10, 90, 280, 400, 550, 730, 880]

imgs = os.listdir(src_path)
#imgs = filter(lambda x: x.endswith('.jpg'), imgs)

for each_img in imgs:
    # get the name of each video, and make the directory to save frames
    each_img_name = each_img.split('.')
    new_name = each_img_name[0].split("local_10_")[-1]
    print(new_name)
    #os.mkdir(videos_save_path + '/' + each_video_name)

    #each_video_save_full_path = os.path.join(videos_save_path, each_video_name) + '/'

    # get the full path of each video, which will open the video tp extract frames
    each_img_full_path = os.path.join(src_path, each_img)
    #print(each_img_full_path)

    img  = cv2.imread(each_img_full_path)
    a = img.shape
    p = cv2.resize(img, (int(a[1] / 10), int(a[0] / 10)),interpolation=cv2.INTER_CUBIC)
    #print("%s%s.jpg" % (save_path, str(i+1)))
    cv2.imwrite("%s%s.jpg" % (save_path, new_name), p)