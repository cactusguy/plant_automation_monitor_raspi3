import automationhat
import time
while True:
    automationhat.relay.two.on()
    print ("1")
    time.sleep(3600)
    automationhat.relay.two.off()
    print ("2")
    time.sleep(7200)
