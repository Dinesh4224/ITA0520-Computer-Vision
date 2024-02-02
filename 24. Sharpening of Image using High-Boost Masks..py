import cv2
resized_img = cv2.imread("E:/computer vision/programs/4.Dilate function.jpg")
resized_wm = cv2.imread("E:/computer vision/programs/5.Erode function.jpg")

h_img, w_img, _ = resized_img.shape
center_y = int(h_img/2)
center_x = int(w_img/2)
h_wm, w_wm, _ = resized_wm.shape
top_y = center_y - int(h_wm/2)
left_x = center_x - int(w_wm/2)
bottom_y = top_y + h_wm
right_x = left_x + w_wm

roi = resized_img[top_y:bottom_y, left_x:right_x]

resized_wm = cv2.resize(resized_wm, (roi.shape[1], roi.shape[0]))

result = cv2.addWeighted(roi, 1, resized_wm, 0.3, 0)
resized_img[top_y:bottom_y, left_x:right_x] = result

filename = "D:\Shiva\CV\EX 2.jpg"
cv2.imwrite(filename, resized_img)

cv2.imshow("Resized Input Image", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
