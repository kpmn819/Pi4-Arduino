#!/usr/bin/env python3
# ------------ IMPORTS -----------------

import time
import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)
# ---------- END IMPORTS --------------------

# ---------- CLASS DEFINITIONS --------------
# may need to make a Sim_key class
# key_function = what it does
# there are really on two things required here
# the modifier key(s) and the main key
# the modifier is one byte with various bits set for the keys
class Sim_key:
  def __init__(self, key_mod, key_code):
    self.key_mod = key_mod
    self.key_code = key_code
    self.key_mod = key_mod
    self.key_code = key_code
# need some major dictionary to look up the numerics
ap_on_key = Sim_key("ctl","shf")
# this is a level of abstraction before converting to the actual number lookup
# that will require passing the Sim_key object to a parser that will compile 
# the actual codes


# --------- END CLASS DEFINITIONS ------------


# ---------- VARIABLE DECLARATIONS ------------
NULL_CHAR = chr(0)
s = 0.5
# key dictionary first the modifiers
mod_dict = {'nul':0,
'shf':32, 
'ctl':1,
'alt':4,
'ctlshf':3,
'altshf':6}
# now the letter and other physical keys
key_dict = {'a':4,
'b':5,
'c':6,
'r':21,
't':23,
'z':29,}
# --------END VARIABLE DECLARATIONS

# ----------- METHODS ------------------
def write_report(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())
        
        

def make_key(char1,char2,char3):
    # compose the final key_code here
    pass




# --------- END METHODS -----------------

# ---------- MAIN PROGRAM START -------------
def main(): # The actual main program
    print('main program running no other guy')

    which_one = input("Choose a number ")
    print('which one is'+ which_one)
    if which_one == '1':
        # Press a single char
        write_report(NULL_CHAR*2+chr(21)+NULL_CHAR*5)
        print('routine 1')
        # Release keys
        write_report(NULL_CHAR*8)
        time.sleep(s)
    
    if which_one== '2':
        # Press SHIFT + a = A
        write_report(chr(32) + NULL_CHAR + chr(9) + NULL_CHAR * 5)
        
        print('routine 2')
        # Release all keys
        write_report(NULL_CHAR*8)
        time.sleep(s)

    if which_one=='3':
        
        write_report(chr(6) + NULL_CHAR + chr(18) + NULL_CHAR * 5)
        print('routine 3')
        time.sleep(s)
        # Release all keys
        write_report(NULL_CHAR*8)

# ------------ END MAIN PROGRAM -----------------

if __name__ == "__main__":
    # If this is being run stand-alone then execute otherwise it is being
    # imported and the importing program will use the modules it needs
    main() # Invoke the program
