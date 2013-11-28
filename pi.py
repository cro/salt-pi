# -*- coding: utf-8 -*-
'''
Functions for a Raspberry Pi
'''

# Import python libs
import os
HAS_RPI = False
try:
    import RPi.GPIO as GPIO
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
