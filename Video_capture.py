import cv2



cam = cv2.VideoCapture(0,cv2.CAP_DSHOW) ## 카메라 끌떄 오류 안나오도록 

if not cam.isOpened():
    print("Could not open webcam")
    exit()

while cam.isOpened():
    status, frame = cam.read()

    if status:
        cv2.imshow("test", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()


