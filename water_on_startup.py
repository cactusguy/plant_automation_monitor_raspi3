print ("start1")
import automationhat
x = automationhat.analog.one.read()
while True:
    while x < 3.24:
        automationhat.relay.one.on()
    
