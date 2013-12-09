# -*- coding: utf-8 -*-
'''
Functions for a Raspberry Pi

    :codeauthor: :email:`Dave Boucha (dave@saltstack.com)`
    :codeauthor: :email:`C. R. Oldham (cr@saltstack.com)`
    :copyright: © 2013 by SaltStack, Inc.
    :license: Apache 2.0, see LICENSE for more details.

    This module supports very simple integration with a Raspberry Pi.
    You can detect a GPIO pin status, or send data over the i2c bus
    as an i2c master.

'''

# Import python libs
import os
import time

HAS_RPI = False
try:
    import RPi.GPIO as GPIO
    import smbus
    GPIO.setmode(GPIO.BCM)
    HAS_RPI = True
except ImportError:
    pass

# Define the module's virtual name
__virtualname__ = 'pi'


def __virtual__():
    '''
    Only work on Raspberry Pi hardware
    '''
    if HAS_RPI:
        return 'pi'
    return False


def _i2c_init(rpi_version=2):
    '''
    Initialize the i2c bus.  There are two versions of the Raspberry Pi Model B.
    The original 256 MB version located the i2c bus at port 0, the more common
    512 MB one locates it at port 1.

    After we init, we store the bus object in the minion __context__ enabling us
    to retrieve it without reinitializing
    '''

    if 'i2c' not in __context__:

        if rpi_version == 1:
            # for RPI version 1 init port at 0
            bus = smbus.SMBus(0)
        else:
            # for RPI version 2, init i2c at port 1
            bus = smbus.SMBus(1)

        __context__['i2c'] = bus
        return bus
    else:
        return __context__['i2c']


def i2c_write(address, value):
    '''
    Write to the i2c bus.  We need an address to write to.
    i2c supports up to 256 devices on the bus.
    Note that this function wraps several i2c functions.
    By default i2c writes one 8-bit byte at a time.
    You can also write a word (16-bits) or a block 
    (up to 32 bytes)
    '''

    bus = _i2c_init()

    bus.write_byte(0x04, value)
    return True

def i2c_read(address):
    '''
    Read from the i2c bus.
    '''

    bus = _i2c_init()

    return bus.read_byte(0x04)
    return value

def _setup_pin(pin):
    '''
    Set up the pin for input
    '''
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.IN)
    return True


def pin_status(pin):
    '''
    Get pin status

    CLI Example:

    .. code-block:: bash

        salt '*' pi.pin_status 23
    '''
    _setup_pin(pin)
    return GPIO.input(pin)


def victory():
    '''
    Play the Final Fantasy Victory Fanfare!!
    mp3 file is not included with this module.

    CLI Example:

    .. code-block:: bash

        salt '*' pi.victory
    '''
    return os.system('mpg321 /home/pi/FinalFantasyV-VictoryFanfare.mp3')


def khan():
    '''
    Play Khan!!!!!!!!!!!!!
    mp3 file is not included with this module.

    CLI Example:

    .. code-block:: bash

        salt '*' pi.khan
    '''
    return os.system('mpg321 /home/pi/Khan.mp3')
