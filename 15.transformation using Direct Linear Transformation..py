import cv2
import numpy as np
from numpy.linalg import svd

def dlt_transform(src_points, target_points):
    
    if len(src_points) != len(target_points) or len(src_points) < 4:
        raise ValueError("Invalid number of points or insufficient correspondences for DLT.")

    src_points_homog = np.hstack((np.array(src_points), np.ones((len(src_points), 1))))
    target_points_homog = np.hstack((np.array(target_points), np.ones((len(target_points), 1))))

    A = []
    for i in range(len(src_points_homog)):
        x, y, w = src_points_homog[i]
        xp, yp, wp = target_points_homog[i]
        A.append([-x, -y, -w, 0, 0, 0, x * xp, y * xp, w * xp])
        A.append([0, 0, 0, -x, -y, -w, x * yp, y * yp, w * yp])

    A = np.array(A)

    _, _, V = svd(A)

    H = V[-1, :].reshape((3, 3))

    return H

 
pts1 = np.array([[50, 50], [200, 50], [50, 200], [200, 200]])
pts2 = np.array([[100, 100], [300, 100], [100, 300], [300, 300]])

# Perform DLT transformation
H = dlt_transform(pts1, pts2)

# Load images
img1 = cv2.imread("E:/computer vision/programs/4.Dilate function.jpg")
img2 = cv2.imread("E:/computer vision/programs/5.Erode function.jpg")

# Warp the first image using the obtained transformation matrix
dst = cv2.warpPerspective(img1, H, (img2.shape[1], img2.shape[0]))

# Display images
cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
