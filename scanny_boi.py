#! /usr/bin/python3

#Import modules

import os
import sane
from PIL import Image

#Print Title
print("Sanny Boi")

#variables for parameters

depth = 8
mode = input("Input 'color' or 'gray':")
source = "Transparency Unit"
film_type = "Negative Film"
focus_position ="Focus 2.5mm above glass"
#position of upper left corner of first frame
x = 2 
ystart = 26

#Set directory edit prefix to set default parent directory
prefix = os.getenv("HOME") + "/Pictures/Scans/"
print("Working directory is:", prefix)
directory = input("Input the name of the directory within the working directory in  which to store scans (directory must already exist):")
path = prefix + directory

#xdim = int
#ydim = int
#xinc = int
#xinc2 = int
#yinc = int
#smax = int
#frames = int

#Set Format
format = input("Input film format(35,645,66,67,69(nice))")
format = (int(format))
if format == 35:
    ystart  = 16
    xdim = 28
    ydim = 40
    xinc = 37
    xinc2 = 43.5
    yinc = 38
    smax = 4
    frames = 6
elif format == 645:
    xdim = 65
    ydim = 50
    xinc = 82
    yinc = 50
    smax = 2
    frames = 4
elif format == 66:
    xdim = 65
    ydim = 65
    xinc = 82
    yinc = 65
    smax = 2
    frames = 3
elif format == 67:
    xdim = 65
    ydim = 75
    xinc = 82
    yinc = 75
    smax = 2
    frames = 2
elif format == 69:
    xdim = 65
    ydim = 75
    xinc = 82
    yinc = 95
    smax = 2
    frames = 1
print (xdim,ydim,xinc,yinc,smax,frames)
#frame number
num = input("Input starting number:")
n = int(num)

#number of strips
strips = input("Input number of strips:")
try:
    s = int(strips)
except:
    print("Enter a number")
    quit()
if s > smax:
    print ("Too many strips")
    quit()
    
resolution = input("Input resolution see readme for options:")

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
    dev.tl_y = ystart
except:
    print("cannot set position, using default")
try:
    dev.resolution = int(resolution)
except:
    print("cannot set resolution, using defult")

params = dev.get_parameters()
print('Device parameters:', params)

#print(dev.optlist) #left in for scanner options visibility

#dev.start()
#scan loops outer loop iterates across film strips, inner loop iterates frames
i = 1
while i <= s:
    j = 1
    y = int(ystart)
    dev.tl_x = x
    dev.tl_y = y
    while j <= frames:
        dev.br_x = dev.tl_x + xdim
        dev.br_y = dev.tl_y + ydim
        filename = path +"/" + f"{n:04d}" + ".tiff"

#start scan
        dev.start()
        im = dev.snap()
        im.save(filename)
        print(filename, "captured")
        y += yinc
        dev.tl_y = y
        n += 1
        j += 1
    if i % 2 == 0:
        x += xinc2
    else:
        x += xinc
   # dev.tl_x = x
    i += 1
print("Done!")
#close device and exit
dev.close()        
sane.exit()

    
