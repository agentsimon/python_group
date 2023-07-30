#!/usr/bin/env python3
# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.

import time
from rpi_ws281x import PixelStrip, Color
import argparse
import cv2

vid = cv2.VideoCapture(0)
# LED strip configuration:
LED_COUNT = 100        # Number of LED pixels.
LED_PIN = 18          # GPIO pin connected to the pixels (18 uses PWM!).
# LED_PIN = 10        # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
rev2 = []

# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=1):
    """Wipe color across display a pixel at a time."""
    for i in range(LED_COUNT):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms / 1000.0)




# Main program logic fololows
    # Create NeoPixel object with appropriate configuration.
strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
strip.begin()
print('Color wipe animations.')
colorWipe(strip, Color(255, 0, 0))  # Red wipe
colorWipe(strip, Color(0, 255, 0))  # Green wipe
colorWipe(strip, Color(0, 0, 255))  # Blue wipe
colorWipe(strip,Color(255,255,255)) # White wipe
print("Press Ctrl-C to quit")

while True:
            
            # define a video capture object
    ret, frame1 = vid.read()
    #im_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame =cv2.resize(frame1,(10, 10), interpolation = cv2.INTER_LINEAR)
#    cv2.imshow('frame', frame)
    position = 0
    color = []
    for x in range (0,frame.shape[1],1):
        for y in range(0,frame.shape[0],1):
            (blue,green,red) = frame[y,x]
#       color.insert(position,(green,red,blue))
            strip.setPixelColorRGB((x*y),red,green,blue)                
            position = position +1
#     for x in range(0,100,20):
#   rev2 = rev2 + color[x:x+10] + color[x+10:x:-1]
#       print("List is ", rev2)
    # Do the Neopixel stuff
#   for X1 in range(len(rev2)):
#       red = rev2[X1][1]
#       green = rev2[X1][0]
#       blue = rev2[X1][2]
#       strip.setPixelColorRGB(X1,red,green,blue)
        
    strip.show()

    if cv2.waitKey(1) & 0xFF == ord('c'):
        break
# Turn all the LEDs to black
coloWipe(strip, Color(0,0,0))
strip.show()
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
