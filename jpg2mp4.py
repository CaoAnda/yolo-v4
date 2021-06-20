import cv2
# 输出路径
fps = 25
filename = "MVI_39401"
num = 1385
videowrite = cv2.VideoWriter(r'D:\Desktop\%s_%d.mp4'%(filename, fps),-1, fps, (960,540))#，size是图片尺寸

img_array=[]
from tqdm import tqdm
for filename in tqdm([r'E:\{}\img{:0>5d}.jpg'.format(filename,i) for i in range(1,num + 1)]):
    img = cv2.imread(filename)
    if img is None:
        print(filename + " is error!")
        continue
    img_array.append(img)
for i in tqdm(range(num)):
    videowrite.write(img_array[i])
print('end!')