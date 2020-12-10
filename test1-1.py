# ------------- BEGIN IMPORTS ------------------
import smbus
import time  
import sys
import RPi.GPIO as GPIO
# ------------ END IMPORTS -----------------------
# --------BEGIN ASSIGNMENTS AND VARIABLES --------
bus = smbus.SMBus(1)
address = 0x04              # Arduino I2C Address

# --------- BEGIN METHODS AND FUNCTIONS -----------

# ----------- END METHODS AND FUNCTIONS -----------

# ^^^^^^^^^^^^^^ BEGIN MAIN PROGRAM ^^^^^^^^^^^^^^^
def main():  
    i2cData = False  
    while 1:  
        # analog ports go from 0 - 6, Digital Inputs from 22 - 30
        # Digital Outputs toggle on/off 40 - 50
        data_to_send = int(input('Enter data to send '))
        time.sleep(.2)
        # this sends out our actual port request number
        # with bad input filtered out
        if ((data_to_send >= 0 and data_to_send <= 6) or (data_to_send >= 22 and data_to_send <= 30) or
        (data_to_send >= 40 and data_to_send <= 50)):
            bus.write_byte(address, data_to_send)

            # request data from arduino via i2c
            print("Arduino answer to RPi:", bus.read_byte(address))
        else:
            print('Bad input not in Range')


# ^^^^^^^^^^^^^^^^ END MAIN PROGRAM ^^^^^^^^^^^^^^^^^^^^^^

if __name__ == '__main__':  
    try:  
        main()  
    except KeyboardInterrupt:  
        GPIO.cleanup()
        sys.exit(0)
