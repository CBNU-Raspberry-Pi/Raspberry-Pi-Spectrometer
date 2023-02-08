# Raspberry Pi OS Download
## Raspberry Pi Imager Download
[Raspberry Pi Imger Download Site](https://www.raspberrypi.com/software/)에 들어가서 OS에 맞는 Raspberry Pi Imager를 다운 받는다.

![Raspberry Pi Imger Download](https://github.com/CBNU-Raspberry-Pi/Raspberry-Pi-Spectrometer/blob/main/setting%20img/Raspberry%20Pi%20Imager.png "Raspberry Pi Imger download 이미지")

## Raspberry Pi OS Download
다운 받은 Raspberry Pi Imager를 열면 다음과 같은 화면이 나타나게 된다. 

![Raspberry Pi Imger 화면](https://github.com/CBNU-Raspberry-Pi/Raspberry-Pi-Spectrometer/blob/main/setting%20img/Raspberry%20Pi%20OS_1.png "Raspberry Pi Imger 화면") 

**운영체제 선택** 버튼을 클릭한다. 그러면 다음과 같은 화면이 나타나게 된다.

![Raspberry Pi Imger 운영체제 선택 화면](https://github.com/CBNU-Raspberry-Pi/Raspberry-Pi-Spectrometer/blob/main/setting%20img/Raspberry%20Pi%20OS_2.png "Raspberry Pi Imger 운영체제 선택 화면")

가장 상단에 있는 **Raspberry Pi OS (32-bit)**를 선택한다. 

(이 문서에서는 2022-09-22에 릴리즈된 OS를 사용하였음)


운영체제를 선택한 뒤, **저장소 선택** 버튼을 클릭한다. 그러면 다음과 같은 화면이 나타나게 된다.

![Raspberry Pi Imger 저장소 선택 화면](https://github.com/CBNU-Raspberry-Pi/Raspberry-Pi-Spectrometer/blob/main/setting%20img/Raspberry%20Pi%20OS_3.png "Raspberry Pi Imger 저장소 선택 화면")

원하는 저장소를 선택하고, 쓰기 버튼을 누른다.

![Raspberry Pi Imger 주의 화면](https://github.com/CBNU-Raspberry-Pi/Raspberry-Pi-Spectrometer/blob/main/setting%20img/Raspberry%20Pi%20OS_4.png "Raspberry Pi Imger 주의 화면")

다음과 같은 화면이 나오면, **예**를 누른 뒤 OS를 다운 받는다.

(혹시 중요한 파일이 SD카드에 있는 경우 백업을 해두는 것이 좋음)

# Raspberry Pi Setting
## SD 카드 삽입

OS를 다운 받은 SD카드를 다음 위치에 방향을 맞추어 삽입한다. 

![Raspberry Pi](https://github.com/CBNU-Raspberry-Pi/Raspberry-Pi-Spectrometer/blob/main/setting%20img/Raspberry%20Pi%20Setting_1.png "Raspberry Pi")

![Raspberry Pi SD카드 삽입](https://github.com/CBNU-Raspberry-Pi/Raspberry-Pi-Spectrometer/blob/main/setting%20img/Raspberry%20Pi%20Setting_2.png "Raspberry Pi SD카드 삽입")

## 카메라 설치

은색 면이 화면 포트쪽으로 오도록 카메라를 연결한다. 

![Raspberry Pi 카메라 연결](https://github.com/CBNU-Raspberry-Pi/Raspberry-Pi-Spectrometer/blob/main/setting%20img/Raspberry%20Pi%20Setting_3.gif "Raspberry 카메라 연결")


# Raspberry Pi 초기 설정

라즈베리파이를 키면 다음과 같은 화면이 나타난다. 

다음의 방식으로 Raspberry Pi를 세팅한다. 

![Raspberry Pi 화면_1](https://github.com/CBNU-Raspberry-Pi/Raspberry-Pi-Spectrometer/blob/main/setting%20img/Raspberry%20Pi%20Setup_1.png)

* **Next** 버튼을 누른다.

![Raspberry Pi 화면_2](https://github.com/CBNU-Raspberry-Pi/Raspberry-Pi-Spectrometer/blob/main/setting%20img/Raspberry%20Pi%20Setup_2.png)

* **Use English language** 를 선택하고, **Next** 버튼을 누른다.

![Raspberry Pi 화면_3](https://github.com/CBNU-Raspberry-Pi/Raspberry-Pi-Spectrometer/blob/main/setting%20img/Raspberry%20Pi%20Setup_3.png)

* username: **RaspberryPi**, password: **12345678**로 설정하고, **Next** 버튼을 누른다. (라즈베리파이는 동아리 소유의 물품이므로 **username과 password**를 통일함)

![Raspberry Pi 화면_4](https://github.com/CBNU-Raspberry-Pi/Raspberry-Pi-Spectrometer/blob/main/setting%20img/Raspberry%20Pi%20Setup_4.png)
* **Next** 버튼을 누른다.

![Raspberry Pi 화면_5](https://github.com/CBNU-Raspberry-Pi/Raspberry-Pi-Spectrometer/blob/main/setting%20img/Raspberry%20Pi%20Setup_5.png)
* 연결하고 싶은 와이파이를 선택하고, **Next**버튼을 누른다.
* 인터넷 연결이 없으면, 카메라 모듈을 실행하기 위한 파일을 설치할 수 없다.

![Raspberry Pi 화면_6](https://github.com/CBNU-Raspberry-Pi/Raspberry-Pi-Spectrometer/blob/main/setting%20img/Raspberry%20Pi%20Setup_6.png)
* **Next**버튼을 누른다.

# 카메라 모듈 실행을 위한 설정

## libcamera setting
1. OS 업데이트 및 업그레이드
   
   터미널에 다음 명령어를 작성하여, OS를 업데이트 및 업그레이드한다.
   ```
   sudo apt update
   ```
   ```
   sudo apt full-upgrade
   ```
2. 라즈베리파이 설정하기
   ```
   sodo raspi-config
   ```
   ![Raspberry Pi config 화면_1](https://github.com/CBNU-Raspberry-Pi/Raspberry-Pi-Spectrometer/blob/main/setting%20img/Raspberry%20Pi%20config_1.png)
   * 다음 화면에서 **Advanced Options**를 선택한다.
   * **Glamor**를 선택하여, glamor graphic을 활성화시킨다.
   * 다시  **Advanced Options**를 선택한다.
   * **GL Driver**를 선택한 뒤, **GL (Full KMS)** 선택한다.
   * **Finish**를 선택하여, 라즈베리파이를 reboot한다.


3. config.txt 변경
   
   * 터미널에 다음 명령어를 작성하여, config.txt 파일에 접근한다.
     ```
     sudo nano /boot/config.txt
      ```
   * 파일에서  "dtoverlay=vc4-kms-v3d"을 "dtoverlay=ov9281"로 변경한다.
   * ctrl+x를 눌러 nano에서 벗어난다.
   * 변경한 내용을 y를 눌러서 저장하고, enter를 누른다. 
   * 터미널에 다음 명령어를 작성하여, 라즈베리파이를 리부팅한다.
      ```
     sudo reboot
      ```

4. libcamera 실행하기
   ```
   libcamera-hello
   ```
   다음 명령어를 통해 5초 동안 카메라를 확인할 수 있다. 이때, 카메라 화면이 나타나지 않고 에러가 발생할 경우 **2. 라즈베리파이 설정하기** 부분을 다시 실행하도록한다.


   ```
   libcamera-hello -t 0
   ```
   다음 명령어를 통해 지속적으로 카메라를 확인할 수 있다. 이를 끌 때는 ctrl+c를 터미널 창에 작성한다.

   
## picamera2 및 Opencv 설치하기

1. 다음을 터미널에서 실행하여 picamera2를 설치한다.

       sudo apt install -y python3-libcamera python3-kms++
       sudo apt install -y python3-pyqt5 python3-prctl libatlas-base-dev ffmpeg  python3-pip
       pip3 install numpy --upgrade
       pip3 install picamera2

2. 다음을 터미널에서 실행하여 opencv를 다운 받는다.
   
       sudo apt install -y python3-opencv
       sudo apt install -y opencv-data
       pip3 install tflite-runtime

다음의 과정을 진행한 뒤 아래 코드를 실행한다. 이 코드는 github에 올려두었다.

``` python
import cv2
from picamera2 import Picamera2

cv2.startWindowThread()

picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
picam2.start()
picam2.set_controls({"FrameDurationLimits": (33333, 33333)})
# 상단의 코드는 프레임속도 조절 코드로 없으면 에러가 나온다. 주의 부탁!
while True:
    im = picam2.capture_array()
    cv2.imshow("Camera", im)
    if cv2.waitKey(1) == ord('q'):
        break

        
cv2.destroyAllWindows()

``` 

이때, 카메라 화면이 나타나지 않고 에러가 발생할 경우 **libcamera setting의 2. 라즈베리파이 설정하기** 부분을 다시 실행하도록 한다.

**다시 문제가 발생할 경우 송다현 학생에게 연락부탁드립니다.**
