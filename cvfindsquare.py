import cv2


def detect_square(frame,image):
    #image = cv2.resize(frame,(0,0),fx=0.5,fy=0.5)
    found,corners = cv2.findChessboardCorners(frame,(7,7),flags=cv2.CALIB_CB_FAST_CHECK)
    if found:
        x = int(corners[24][0][0])
        y = int(corners[24][0][1])
        frame[y:y+image.shape[0],x:x+image.shape[1]] = image

    return frame

webcam_cap = cv2.VideoCapture(0)
video = cv2.VideoCapture("/home/james/Videos/final_deployment.mp4")
while True:
    ret,frame = webcam_cap.read()
    ret_v,video_overlay = video.read()
    image = cv2.resize(video_overlay,(0,0),fx=0.1,fy=0.1)
    if ret == True:
        detect_square(frame,image)
        cv2.imshow('Video',frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break