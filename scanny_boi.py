#! /usr/bin/python3

#Import functions

#from__future__ import print_function
import sane
from PIL import Image

#variables for parameters

depth = 8
mode = input("Input color or grey:")
source = "Transparency Unit"
film_type = "Negative Film"
focus_position ="Focus 2.5mm above glass"
resolution = input("Input resolution50|60|72|75|80|90|100|120|133|144|150|160|175|180|200|216|240|266|300|320|350|360|400|480|600|720|800|900|1200|1600|1800|2400|3200)")
#position of upper left corner of first frame
x = 2 
y = 16

#Set directory
prefix = "/home/royle/Pictures/Scans/"
directory = input("Input the name of the directory in which to store scans (directory must already exist):")
path = prefix + directory

#frame number
num = input("Input starting number:")
n = int(num)

#number of strips
strips = input("Input number of strips(1:4):")
try:
    s = int(strips)
except:
    print("Enter a number")
    quit()
if s > 4:
    print ("Number must be less than 4")
    quit()

# initialize SANE
ver =sane.init()
print("SANE version:", ver)

#Get Devices
devices = sane.get_devices()
print("Available devices:", devices)

#Open first device
dev = sane.open(devices[0][0])

print(dev)

#set options

params = dev.get_parameters()
try:
    dev.Depth = depth
except:
    print("cannot set depth defaulting to %d" % params[3])

try:
    dev.mode = mode
except:
    print("cannot set mode, defaulting to %s" % params[0])

try:
    dev.source = source
except: print("cannot set source using default")

try:
    dev.focus_position = focus_position
except:
    print("cannot set focus position using default")

try:
    dev.film_type = film_type
except:
    print("cannot set film tipe using default")

try:
    dev.tl_x = x
    dev.tl_y = y
except:
    print("cannot set position, using default")
try:
    dev.resolution = resolution
except:
    print("cannot set resolution, using defalut")
#try:
    #dev.br_x = 215.9
    #dev.br_y = 297.18
    #dev.br_x = dev.tl_x + 28
    #dev.br_y = dev.tl_y + 40
#except:
   #print("cannot set size, using default")

params = dev.get_parameters()
print('Device parameters:', params)
#print(dev.optlist)
#dev.start()
#scan loops outer loop iterates across film strips, inner loop iterates frames
i = 1
while i <= s:
    j = 1
    y = 16
    dev.tl_x = x
    dev.tl_y = y
    while j <= 6:
        dev.br_x = dev.tl_x + 28
        dev.br_y = dev.tl_y + 40
        filename = path +"/" + str(n) + ".tiff"

#start scan
        dev.start()
        im = dev.snap()
        im.save(filename)
        print(filename, "captured")
        y += 38
        dev.tl_y = y
        n += 1
        j += 1
    if i % 2 == 0:
        x += 43.5
    else:
        x += 37
   # dev.tl_x = x
    i += 1

#close device and exit
dev.close()        
sane.exit()

    
