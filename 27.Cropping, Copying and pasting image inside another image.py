import cv2

# Load main image
main_image = cv2.imread("E:/computer vision/programs/5.Erode function.jpg")

if main_image is not None:
    # Get dimensions of the main image
    main_height, main_width, _ = main_image.shape

    # Define the region to crop from the main image
    crop_height, crop_width = 80, 288
    cropped_region = main_image[0:crop_height, 0:crop_width]

    # Load the image to be pasted
    paste_image = cv2.imread("E:/computer vision/programs/4.Dilate function.jpg")

    if paste_image is not None:
        # Define the position to paste the image in the main image
        paste_x, paste_y = main_width - paste_image.shape[1], main_height - paste_image.shape[0]

        # Ensure the dimensions match and paste the region onto the main image
        main_image[paste_y: paste_y + cropped_region.shape[0], paste_x: paste_x + cropped_region.shape[1]] = cropped_region

        # Display the result
        cv2.imshow("Result", main_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Error: Could not load paste image.")
else:
    print("Error: Could not load main image.")
