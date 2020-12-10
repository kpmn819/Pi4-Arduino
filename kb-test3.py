import time
import RPi.GPIO as GPIO

# We are going to use the BCM numbering
GPIO.setmode(GPIO.BCM)

# Set pin 26 as input using pull up resistor
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
print("I am running")

# function to send the data
def write_report(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())

# infinite loop to check the pins and send data
while True:
    if not(GPIO.input(18)):
        
        # shift-cmd-5
        shift_cmd_5 = str(0b01010000) + "\0\x22\0\0\0\0\0"
        write_report(shift_cmd_5)
        print("SNAP!!")
        time.sleep(0.2)
        write_report("\0\0\0\0\0\0\0\0")
