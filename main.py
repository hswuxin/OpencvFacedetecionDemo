import cv2

#视频流
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()  # 读取一帧数据
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 将图片转化成灰度

    #人脸
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
    face_cascade.load('D:\DC\opencv-facedetecionDemo\haarcascade_frontalface_alt2.xml')  # 一定要告诉编译器文件所在的具体位置
    '''此文件是opencv的haar人脸特征分类器'''
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    #带着眼镜的眼镜
    eye_glasses=cv2.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")
    eye_glasses.load("D:\DC\opencv-facedetecionDemo\haarcascade_eye_tree_eyeglasses.xml")
    eyeGlasses=eye_glasses.detectMultiScale(gray, 1.3, 5)

    #普通眼睛
    eye_default = cv2.CascadeClassifier("haarcascade_eye.xml")
    eye_default.load("D:\DC\opencv-facedetecionDemo\haarcascade_eye.xml")
    eyeDefault = eye_default.detectMultiScale(gray, 1.3, 5)

    #侧视
    side_face = cv2.CascadeClassifier("haarcascade_profileface.xml")
    side_face.load("D:\DC\opencv-facedetecionDemo\haarcascade_profileface.xml")
    sideFace = side_face.detectMultiScale(gray, 1.3, 5)


    if len(faces) > 0:
        for (x, y, w, h) in faces:

            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    if len(eyeGlasses) > 0:
        for (x, y, w, h) in eyeGlasses:

            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    if len(eyeDefault) > 0:
        for (x, y, w, h) in eyeDefault:

            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    if len(sideFace) > 0:
        for (x, y, w, h) in sideFace:

            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)



    cv2.imshow("capture", frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

                # 释放摄像头并销毁所有窗口
cap.release()
cv2.destroyAllWindows()