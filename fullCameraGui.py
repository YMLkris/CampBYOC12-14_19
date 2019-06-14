from guizero import *
from picamera import PiCamera, Color
from time import sleep

camera=PiCamera()
camera.rotation=180

def startPreview():
    camera.image_effect=effectType.value
    camera.start_preview(alpha=225)

def stopPreview():
    camera.stop_preview()

def startVideo():
    camera.image_effect=effectType.value
    sleep(float(delayTime.value))
    camera.start_recording('/home/pi/Desktop/video.h264')

def stopVideo():
    camera.stop_recording()

def quitProgram():
    sys.exit()

def takeStill():
    camera.image_effect=effectType.value
    sleep(float(delayTime.value))
    camera.capture('/home/pi/Desktop/image.jpg')

app = App(title='My Camera', width = 300, height = 300, layout='grid', bg='lightblue')
textTitle = Text(app, text='Camera Controller', grid=[1,0])
stPreButton=PushButton(app,command=startPreview, text='Start Preview',grid=[1,1])
stopPreButton=PushButton(app,command=stopPreview, text='Stop Preview', grid=[2,1])
takeStillButton=PushButton(app,command=takeStill, text='Take Still', grid=[1,2])
startVideoButton=PushButton(app,command=startVideo, text='Start Video', grid=[1,3])
stopVideoButton=PushButton(app, command=stopVideo, text='Stop Video', grid=[2,3])
quitButton=PushButton(app, command=quitProgram, text='Quit', grid=[1,5])
effectType = Combo(app, options=["none","negative", "sketch", "oilpaint"], selected="none", grid=[1,4])
delayTime=TextBox(app, text='0', grid=[2,3])
app.display()