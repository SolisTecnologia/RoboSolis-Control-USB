#!/usr/bin/python3
"""
Solis Robot - SoBot

USB_Control.py: Programming example to control the robot solis by a USB remote control.

Created By   : Vinicius M. Kawakami
Version      : 1.0

Company: Solis Tecnologia
"""
import usb.core
import usb.util
from time import sleep
import serial

USB_IF      = 0 # Interface
USB_TIMEOUT = 5 # Timeout in MS

control = [0,0,0,0,0,0,0,0]

flag_start = 0
flag_pause = 0

BTN_LEFT = 0
BTN_RIGHT = 255
BTN_UP = 0
BTN_DOWN = 255
BTN_START = 32
BTN_OPEN = 127

# Config ID to specific controller HID
USB_VENDOR  = 0x0079 # DragonRise Inc.
USB_PRODUCT = 0x0006 # PC TWIN SHOCK Gamepad

# Open Serial port USB
serialUSB = serial.Serial('/dev/ttyACM0', 9600, timeout=0, dsrdtr=False)
serialUSB .flush()

# Find specific HID connected
dev = usb.core.find(idVendor=USB_VENDOR, idProduct=USB_PRODUCT)

endpoint = dev[0][(0,0)][0]

if dev.is_kernel_driver_active(USB_IF) is True:
  dev.detach_kernel_driver(USB_IF)

usb.util.claim_interface(dev, USB_IF)

while True:
  # Control status reading
  try:
    control = dev.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize, USB_TIMEOUT)
    print(control)
  except:
    pass
  # Check the Start button
  if (control[6] == BTN_START):
    if flag_start == 0:
      flag_start = 1
      serialUSB.write(b"MT0 ME1")
    else:
      flag_start = 0
      serialUSB.write(b"MT0 ME0")
    # Waits for the button to be released
    while (control[6] == BTN_START):
      sleep(0.1)
      try:
        control = dev.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize, USB_TIMEOUT)
        print(control)
      except:
        pass
  # Check the Left button
  if (((control[0]) == BTN_LEFT) and ((control[1]) == BTN_OPEN)):
    flag_pause = 1
    serialUSB.write(b"MT0 ML")
    # Waits for the button to be released
    while (control[0] == BTN_LEFT):
      sleep(0.1)
      try:
        control = dev.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize, USB_TIMEOUT)
        print(control)
      except:
        pass
  # Check the Right button
  elif (((control[0]) == BTN_RIGHT) and ((control[1]) == BTN_OPEN)):
    flag_pause = 1
    serialUSB.write(b"MT0 MR")
    # Waits for the button to be released
    while (control[0] == BTN_RIGHT):
      sleep(0.1)
      try:
        control = dev.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize, USB_TIMEOUT)
        print(control)
      except:
        pass
  # Check the Down button
  elif (((control[1]) == BTN_DOWN) and ((control[0]) == BTN_OPEN)):
    flag_pause = 1
    serialUSB.write(b"MT0 MB")
    # Waits for the button to be released
    while (control[1] == BTN_DOWN):
      sleep(0.1)
      try:
        control = dev.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize, USB_TIMEOUT)
        print(control)
      except:
        pass
  # Check the Up button
  elif (((control[1]) == BTN_UP) and ((control[0]) == BTN_OPEN)):
    flag_pause = 1
    serialUSB.write(b"MT0 MF")
    # Waits for the button to be released
    while (control[1] == BTN_UP):
      sleep(0.1)
      try:
        control = dev.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize, USB_TIMEOUT)
        print(control)
      except:
        pass
  # If no button is pressed, send Pause Movement command one time
  else:
    if(flag_pause == 1):
      flag_pause = 0
      serialUSB .write(b"MT0 MP")

  sleep(0.1) # Let CTRL+C actually exit