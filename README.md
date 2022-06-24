# Solis Robot - SoBot
![](https://github.com/SolisTecnologia/SoBot-USB-Control/blob/master/png/SoBotSingle.png)
# Introduction

AMR (autonomous mobile robotics) platform equipped with a camera system, ultrasonic and photoelectric sensors, works with a high rate of precision and repeatability of its movements, as it uses stepper motors in its movement and navigation, the SoBot also can be termed as a research and development interface, as it facilitates the practical experimentation of algorithms from the simplest to the most complex level.

This product was developed 100% by Solis Tecnologia, and has a lot of technology employing cutting-edge concepts, such as:

The motors can be controlled simultaneously or individually.
The user can select different accessories to implement to the robot.
Several programming languages can be used to connect via API.

# Components

* Main structure in aluminum
* Removable fairing with magnetic attachment points
* Robot Control Driver
* Raspberry Pi 4B board <img align="center" height="30" width="40" src="https://github.com/devicons/devicon/blob/master/icons/raspberrypi/raspberrypi-original.svg">
* 2x NEMA-23 Stepper Motors
* 2x 12V/5A battery
* USB control  <img align="center" height="40" width="40" src="https://github.com/SolisTecnologia/SoBot-USB-Control/blob/master/png/control.png">

# Programming Example
## USB Control - [USB-Control.py](https://github.com/SolisTecnologia/SoBot-USB-Control/blob/master/USB_Control.py)
Programming example to control the robot solis by a USB remote control

The Start button enables and disables robot movement.

The robot moves if any direction button is pressed and when the button is released, the robot stops moving.

### Programming Language

* Python  <img align="center" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg">

### Required Libraries

~~~python
import usb.core
import usb.util
from time import sleep
import serial
~~~

The ''usb.core'' and ''usb.util'' libraries are used to establish connection between the USB remote control and the Raspberry.

The ''time'' library is needed to generate time delays and the ''serial'' library for serial/usb Raspberry connection with the robot controller driver.

### Code Description

The commands used in this example to control SoBot are continuous movement commands, as follows:

~~~python
serialUSB.write(b"MT0 ML")      # Move left
serialUSB.write(b"MT0 MR")      # Move right
serialUSB.write(b"MT0 MB")      # Move backward
serialUSB.write(b"MT0 MF")      # Move Forward
serialUSB.write(b"MT0 MP")      # Pause movement
~~~


For more information about the commands used, check the Robot Commands Reference Guide.


# Reference Link
[SolisTecnologia website](https://solistecnologia.com/produtos/robotsingle)

# Please Contact Us
If you have any problem when using our robot after checking this tutorial, please contact us.

### Phone:
+55 1143040786

### Technical support email: 
contato@solistecnologia.com.br

![](https://github.com/SolisTecnologia/SoBot-USB-Control/blob/master/png/logo.png)