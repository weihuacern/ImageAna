import cv2
import numpy as np

#RGB, white 255,255,255, FFFFFF; 
#Red? 153,0,0, 990000;
#Yellow? 204,204,0, CCCC00;
img = cv2.imread('TestImage/PsiRNA_ori.jpg')
height, width, channels = img.shape
thisedge=691
ystart=24
xstart=6
subimg = img[ystart:(ystart+thisedge), xstart:(xstart+thisedge)]
#img = cv2.imread('TestImage/PsiRNA.jpg')
#for i in range(1,height):
#  for j in range(1,width):
#for j in range(1,width):
#  for i in range(1,height):
#    pixel= img[i,j]
#    if(pixel[0]>245 and pixel[1]>245 and pixel[2]>245):
#      print i,j
#    print pixel
print img.shape
print subimg.shape
cv2.imshow("Image", subimg)
cv2.waitKey(0)
