Scanny Boi (c) 2021 Royle Juusola
Licensed under the MIT license

Description:
Scanny Boi is a simple film scanning automation program.
It currently natively supports 35mm film (medium support to be added eventually) on the Epson Perfection V700
and likely its successors using the stock film holder, other Epson scanners or aftermarket film holders likely
require changing the position of the upper left corner in the code.

Installation:
Install Python3
Install python-sane and pillow using pip or your distribution's repo
Run Scanny_Boi either by invoking it through python, or copy it to /usr/bin/, remove the extension and make it 
executable which will allow execution with the command scanny_boi.

Requirements:
Linux, only tested on Mint
Python3, only tested in Python 3.8.5
python-sane
pillow

Bit depth is set by default to 8, but may be changed to 16 in the code.
Scans are saved by default in HOME/Pictures/Scans with a prompt to name a directory within the default directory, the user input directory must already exist because I am lazy.
The default directory is easily within the code 

Resolution options: 
50|60|72|75|80|90|100|120|133|144|150|160|175|180|200|216|240|266|
300|320|350|360|400|480|600|720|800|900|1200|1600|1800|2400|3200 dpi
