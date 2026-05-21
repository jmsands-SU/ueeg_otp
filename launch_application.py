import RPi.GPIO as GPIO
import time
import subprocess

link=11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(link, GPIO.OUT)

isConnected = True

if not GPIO.input(link):
    GPIO.cleanup()
    quit()
GPIO.cleanup()

if isConnected:
    print("Launch GNU Radio")
    subprocess.run(["/home/pi/Desktop/launch_GNU_UEEG.sh"], shell=True)