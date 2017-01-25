from papirus import Papirus
from papirus import PapirusText

import os
import sys

# Making sure the script is run as root
user = os.getuid()
if user != 0:
    print "Please run script as root"
    sys.exit()
    
# The epaper screen object
screen = Papirus()
screen.set_size(papirus.2_0INCH)

# Update only the changed pixels (faster)
screen.partial_update()

# Papirus text object
text = PapirusText()

# Write text to the screen
text.write("hello world")

# Write text to the screen at selected point
text.write("hello world", (10, 10) )
