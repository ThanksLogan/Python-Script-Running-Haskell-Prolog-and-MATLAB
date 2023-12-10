img = imread('mickey.png');

targetSize = [100,100];
img = imresize (img, targetSize);

img_1d = reshape(img, 1, []);
dlmwrite('input.txt', img_1d, 'delimiter', ' ');

