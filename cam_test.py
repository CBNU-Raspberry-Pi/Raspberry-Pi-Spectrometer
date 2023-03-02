import time
# import picamera
import numpy as np
import cv2
import numpy as np
import matplotlib.pyplot as plt

res = (640, 480)
framerate = 30
exposure_mode = 'off'
exposure_time = 10000  # in microseconds
iso = 100

with picamera.PiCamera() as camera:
    camera.resolution = res
    camera.framerate = framerate
    camera.exposure_mode = exposure_mode
    camera.iso = iso
    time.sleep(2)
    camera.shutter_speed = exposure_time
    camera.exposure_mode = 'off'
    
    # Capture an image
    stream = io.BytesIO()
    camera.capture(stream, format='jpeg', use_video_port=True)
    data = np.fromstring(stream.getvalue(), dtype=np.uint8)
    img = cv2.imdecode(data, 1)

    # Process the image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (3, 3), 0)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    lines = cv2.HoughLines(edges, 1, np.pi/180, 100)

    # Plot the spectrum
    plt.figure()
    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        plt.plot([x1, x2], [y1, y2], 'r')
    plt.xlim(0, res[0])
    plt.ylim(res[1], 0)
    plt.show()


# Set camera parameters
res = (640, 480)
exposure_time = 1000  # in microseconds
iso = 100

# Initialize camera
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, res[0])
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, res[1])
cam.set(cv2.CAP_PROP_EXPOSURE, exposure_time)
cam.set(cv2.CAP_PROP_ISO_SPEED, iso)

# Capture image
ret, img = cam.read()

# Process image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (3, 3), 0)
edges = cv2.Canny(gray, 50, 150, apertureSize=3)
lines = cv2.HoughLines(edges, 1, np.pi/180, 100)

# Plot spectra
plt.figure()
for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))
    plt.plot([x1, x2], [y1, y2], 'r')
plt.xlim(0, res[0])
plt.ylim(res[1], 0)
plt.show()

# Release camera
cam.release()


from picamera2 import Picamera2, Preview
import numpy as np

picam2 = Picamera2()
picam2.configure(picam2.preview_configuration({"size": (640, 480)}))
picam2.start_preview(Preview.QTGL)
overlay = np.zeros((200, 200, 4), dtype=np.uint8)
overlay[:100, 100:] = (255, 0, 0, 64)  # red
overlay[100:, :100] = (0, 255, 0, 64)  # green
overlay[100:, 100:] = (0, 0, 255, 64)  # blue
picam2.set_overlay(overlay)
picam2.start()