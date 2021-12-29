#! /usr/bin/python3

#Import modules

import os
import sane
from PIL import Image
import argparse

#Print Title
print("Sanny Boi")

#argparse args
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", action = "store_true", help = "Verbose Output")
parser.add_argument("-m", "--mode", type = int, help = "1: B/W 2: Color")
parser.add_argument("-d", "--directory", type = str, help = "directory -must already exist")
parser.add_argument("-f", "--format", type = int, help = "Film Format; 35mm: 35, 6x4.5: 645, 6x6: 66, 6x7: 67, 6x9: 69")
parser.add_argument("-n", "--number", type = int, help ="Starting File Number")
parser.add_argument("-s", "--strips", type = int, help ="Number of strips")
parser.add_argument("-r", "--resolution", type = int, help ="Resolution: 50|60|72|75|80|90|100|120|133|144|150|160|175|180|200|216|240|266|300|320|350|360|400|480|600|720|800|900|1200|1600|1800|2400|3200 dpi")

args = parser.parse_args()

#variables for parameters

depth = 8

if args.mode == 2:
    mode = "color"
elif args.mode == 1:
    mode = "gray"
else:
    mode = "gray"
source = "Transparency Unit"
film_type = "Negative Film"
focus_position ="Focus 2.5mm above glass"

#position of upper left corner of first frame
x = 2 
ystart = 26

path = os.getenv("HOME") +"/" + args.directory


#Set Format

if args.format:
    format = args.format
else:
    format = 35
    
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
if args.verbose:
    print (xdim,ydim,xinc,yinc,smax,frames)
#frame number

if args.number:
    n = args.number
else:
    n = 1
#number of strips

if args.strips <= smax:
    s = args.strips
elif args.strips > smax:
    print ("Too many strips, defaulting to max")
    s = smax
else:
    s = smax
    
# resolution
if args.resolution:
    resolution = args.resolution
else:
    resolution = 1600
    
# initialize SANE
ver =sane.init()
if args.verbose:
    print("SANE version:", ver)

#Get Devices
devices = sane.get_devices()
if args.verbose:
    print("Available devices:", devices)

#Open first device
dev = sane.open(devices[0][0])
if args.verbose:
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
if args.verbose:
    print('Device parameters:', params)

#print(dev.optlist) #left in for scanner options visibility


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
        if args.verbose:
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
if args.verbose:
    print("Done!")
    
#close device and exit
dev.close()        
sane.exit()

    
