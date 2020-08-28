import glob
import cv2

img_array = []
second = 1

for filename in sorted(glob.glob("images/*.jpg")):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width, height)
    for tmp in range(second):
        img_array.append(img)

name = 'project.mp4'
out = cv2.VideoWriter(name, cv2.VideoWriter_fourcc(*'MP4V'), 5.0, size)

for i in range(len(img_array)):
    out.write(img_array[i])
out.release()