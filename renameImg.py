import os
import cv2

src_path = 'D:/WorkPlace/ano_pred_cvpr2018/Data/zy1/training/frames/01/'
save_path = 'D:/WorkPlace/ano_pred_cvpr2018/Data/zy1/training/01/'

imgs = os.listdir(src_path)

for each_img in imgs:
    # get the name of each video, and make the directory to save frames
    each_img_name = each_img.split('.')
    new_name = str(int(each_img_name[0])-100)

    # get the full path of each video, which will open the video tp extract frames
    each_img_full_path = os.path.join(src_path, each_img)
    #print(each_img_full_path)

    img  = cv2.imread(each_img_full_path)
    #print("%s%s.jpg" % (save_path, str(i+1)))
    cv2.imwrite("%s%s.jpg" % (save_path, new_name), img)