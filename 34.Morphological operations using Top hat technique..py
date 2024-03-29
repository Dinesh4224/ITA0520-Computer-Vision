import cv2
import numpy as np
image = cv2.imread("E:/computer vision/programs/5.Erode function.jpg", cv2.IMREAD_GRAYSCALE)
if image is not None:
    kernel = np.ones((5, 5), np.uint8)
    top_hat = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel)
    cv2.imshow("Original Image", image)
    cv2.imshow("Top Hat Result", top_hat)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: Could not load the image.")
