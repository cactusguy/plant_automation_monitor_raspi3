print ("start3")
import time
import picamera
while True:
    camera = picamera.PiCamera()
    for i in range(10):
        camera.capture('image{0:04d}.jpg'.format(i))
    time.sleep(3600)
