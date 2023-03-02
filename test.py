import cv2
from picamera2 import Picamera2

cv2.startWindowThread()

picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
picam2.start()
picam2.set_controls({"FrameDurationLimits": (33333, 33333)})
while True:
    im = picam2.capture_array()
    cv2.imshow("Camera", im)
    if cv2.waitKey(1) == ord('q'):
        break

        
cv2.destroyAllWindows()