import cv2
def play_video(video_path, speed=1.0):
    cap = cv2.VideoCapture("D:/mad.mkv")
    if not cap.isOpened():
        print("Error: Could not open video.")
        return
    fps = cap.get(cv2.CAP_PROP_FPS)
    cv2.namedWindow("Video", cv2.WINDOW_NORMAL)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.resizeWindow("Video", frame.shape[1], frame.shape[0])
        cv2.imshow("Video", frame)
        delay = int(1000 / (fps * speed))
        if cv2.waitKey(delay) & 0xFF == 27:  
            break
    cap.release()
    cv2.destroyAllWindows()
play_video('your_video.mp4')  
play_video('your_video.mp4', speed=0.1)  
play_video('your_video.mp4', speed=10.0)  
