Scanny Boi (c) 2021 Royle Juusola
Licensed under the MIT license

Description:
Scanny Boi is a simple film scanning automation program.
It currently natively supports 35mm and 120 film on the Epson Perfection V700
and likely its successors using the stock film holders, other Epson scanners or aftermarket film holders likely
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

