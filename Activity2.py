import cv2
import numpy as np

modifPixVal, modifPixAfter, i = 0, 10, 0

image1path = r'Images/image3.png'
image1 = cv2.imread(image1path, cv2.IMREAD_COLOR)

rows, columns, _ = image1.shape

for x in range(rows):
    for y in range(columns):
        if i < modifPixAfter:
            i+=1
            continue
        image1.itemset((x, y, 0), modifPixVal)
        image1.itemset((x, y, 1), modifPixVal)
        image1.itemset((x, y, 2), modifPixVal)

cv2.imshow('Image 1', image1)
cv2.waitKey(0)

