print ("start3")
import time
import picamera
while True:
    camera = picamera.PiCamera()
    camera.capture('image.jpg')
    time.sleep(3600)