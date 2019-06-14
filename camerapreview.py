from picamera import PiCamera
from time import sleep

#make an instance of the camera

camera = PiCamera()

camera.rotation =180

camera.start_preview(alpha=150)
sleep(5)

for i in range(5):
    sleep(1)
    camera.capture('/home/pi/Desktop/timelapse/image%s.jpg' % i)
camera.stop_preview()

