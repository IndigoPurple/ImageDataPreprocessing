clear;
clc;
close all;

% read info from config file
fp = fopen('config.txt', 'r');
refnum = fscanf(fp, '%d', 1);
localnum = fscanf(fp, '%d', 1);
rects = cell(refnum + localnum, 1);
for i = 1:(refnum + localnum)
    rect = fscanf(fp, '%f', 4);
    rect(1) = rect(1) + 1;
    rect(2) = rect(2) + 1;
    rects{i} = rect;
end
fclose(fp);

% generate objs to read videos
readers = cell(refnum + localnum, 1);
for i = 1:(refnum + localnum)
    if i <= refnum
        videoname = sprintf('ref_%02d.avi', i - 1);
    else
        videoname = sprintf('local_%02d.avi', i - refnum - 1);
    end
    readers{i} = VideoReader(videoname);
end

% get video sizes
sizes = cell(refnum + localnum, 1);
for i = 1:(refnum + localnum)
    sizes{i} = [readers{i}.Width, readers{i}.Height];
end

% calculate final size ratio
ratio = 1;
ratio_second = 1;
for i = 1:(refnum + localnum)
    ratio_w = sizes{i}(1) / rects{i}(3);
    ratio_h = sizes{i}(2) / rects{i}(4);
    ratio = max(ratio, max(ratio_w, ratio_h));
end
ratio = ratio * ratio_second;

% calculate new final rects
newrects = cell(refnum + localnum, 1);
for i = 1:(refnum + localnum)
    newrects{i} = round(rects{i} * ratio);
end

% process frames
ind = 0;
% while hasFrame(readers{1})
while ind == 0
    % read image
    imgs = cell(refnum + localnum, 1);
    for i = 1:(refnum + localnum)
        imgs{i} = readFrame(readers{i});
    end 
    % resize image
    for i = 1:(refnum + localnum)
        imgs{i} = imresize(imgs{i}, [newrects{i}(4), newrects{i}(3)]);
    end 
    % embed local image to reference
    refind = 1;
    for i = 1:localnum
        rect = newrects{i + refnum};
        imgs{refind}(rect(2):(rect(2) + rect(4) - 1), rect(1):(rect(1) + rect(3) - 1), :) ...
            = imgs{i + refnum};
    end
    % write image
    imwrite(imgs{refind}, sprintf('%04d.jpg', ind));
    % imwrite(imgs{refind}(10000:17000, 10000:20000, :), sprintf('%04d_crop.jpg', ind));
    ind = ind + 1;
end

clear;