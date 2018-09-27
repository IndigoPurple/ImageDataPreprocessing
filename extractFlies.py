import os
import shutil

src_path = 'D:/TBSI/2F/data/train_station_img_new/'
save_path = 'D:/TBSI/2F/data/train_station_img/'

sequence = [0, 350, 700, 1100, 1300, 1650, 2000, 2250, 2600, 2800, 2950, 3050, 3250, 3500, 4250, 4600, 5000, 5550, 5800, 6100, 6400, 7000, 7350, 8250, 8750]

for num in sequence:
    files = os.listdir(src_path)
    files = filter(lambda x: x.endswith('%s%d%s' % ('_', num, '.jpg')), files)

    for each_file in files:
        print(each_file)
        #each_file_full_path = os.path.join(src_path, each_file)
        shutil.copy(src_path  + each_file, save_path + each_file)
