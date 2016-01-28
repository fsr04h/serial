import serial
import time
import os

#version3
os.getcwd()
ser = serial.Serial('/dev/ttyACM0', 114200, timeout = 5)

file = open('samples2.csv')
while 1:
 line = file.readline()
 if not line:
        break
 ser.write(line)
 line2 = ser.readline()
 word1, word2, word3 = line2.split(' ') # Split on whitespace
 #print line3
 w0rd1, w0rd2 = word2.split(":")
 w0rd2 = float(w0rd2)
 print w0rd2
 time.sleep(5)
 file.close
