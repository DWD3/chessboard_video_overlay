import cv2

x0 = 20
y0 = 20
x1 = 100
y1 = 100
width = 80
height = 80
def detect_square(frame,image):
    found,corners = cv2.findChessboardCorners(frame,(7,7),flags=cv2.CALIB_CB_FAST_CHECK)
    global x0
    global y0
    global x1
    global y1
    global width
    global height
    if found:
        if corners[0][0][0]<corners[48][0][0] and corners[0][0][1] < corners[48][0][1]:
            x0 = int(corners[0][0][0])
            y0 = int(corners[0][0][1])
            x1 = int(corners[48][0][0])
            y1 = int(corners[48][0][1])
            width = x1-x0
            height = y1-y0
    x_scale = width/image.shape[1]
    y_scale =  height/image.shape[0]
    if x_scale != 0 and y_scale !=0:
        scaled_image = cv2.resize(image,(0,0),fx=x_scale,fy=y_scale)
    else:
        scaled_image = image

    frame[y0:y1, x0:x1] = scaled_image[0:height, 0:width]


    return frame

webcam_cap = cv2.VideoCapture(0)
video = cv2.VideoCapture("/home/james/Videos/sample.mp4")
while True:
    ret,frame = webcam_cap.read()
    ret_v,video_overlay = video.read()
    if ret == True:
        detect_square(frame,video_overlay)
        cv2.namedWindow('Video',cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Video',1280,720)

        cv2.imshow('Video',frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break