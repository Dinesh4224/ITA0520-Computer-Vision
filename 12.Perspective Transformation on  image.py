import cv2
import numpy as np
image = cv2.imread("E:/computer vision/programs/5.Erode function.jpg")
x = 100 
y = 100 
dx = 50  
dy = 30  
while True:
    image_copy = image.copy()
    x += dx
    y += dy
    cv2.imshow('Moving Image', image_copy)
cv2.waitKey() 
cv2.destroyAllWindows()
