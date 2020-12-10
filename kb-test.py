#!/usr/bin/env python3

import time
import RPi.GPIO as GPIO

s = 2

NULL_CHAR = chr(0)

def write_report(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())
print('kb-test is running')
# Press a
write_report(NULL_CHAR*2+chr(4)+NULL_CHAR*5)
time.sleep(s)
# Release keys
write_report(NULL_CHAR*8)
# Press SHIFT + a = A
write_report(chr(32)+NULL_CHAR+chr(4)+NULL_CHAR*5)
time.sleep(s)
# Press b
write_report(NULL_CHAR*2+chr(5)+NULL_CHAR*5)
# Release keys
write_report(NULL_CHAR*8)
time.sleep(s)
# Press SHIFT + b = B
write_report(chr(32)+NULL_CHAR+chr(5)+NULL_CHAR*5)
time.sleep(s)

# Press SPACE key
write_report(NULL_CHAR*2+chr(44)+NULL_CHAR*5)
time.sleep(s)

# Press c key
write_report(NULL_CHAR*2+chr(6)+NULL_CHAR*5)
time.sleep(s)
# Press d key
write_report(NULL_CHAR*2+chr(7)+NULL_CHAR*5)
time.sleep(s)

# Press RETURN/ENTER key
write_report(NULL_CHAR*2+chr(40)+NULL_CHAR*5)
time.sleep(s)

# Press e key
write_report(NULL_CHAR*2+chr(8)+NULL_CHAR*5)
time.sleep(s)
# Press f key
write_report(NULL_CHAR*2+chr(9)+NULL_CHAR*5)
time.sleep(s)

# Release all keys
write_report(NULL_CHAR*8)
