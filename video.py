from picamera import PiCamera, Color
from time import sleep

#make an instance of the camera

camera = PiCamera()
camera.rotation =180
camera.annotate_background = Color('blue')
camera.annotate_foreground = Color('yellow')
camera.annotate_text_size = 60
camera.annotate_text = "Hello World!"
camera.image_effect = 'watercolor'
camera.resolution = (800, 600)
camera.framerate = 20



camera.start_preview(alpha=150)
camera.start_recording('/home/pi/Desktop/video.h264')
sleep(10)
camera.stop_recording()
camera.stop_preview()