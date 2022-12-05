import os, platform

import requests

from os import system as cmd 

os.system('git pull')
bit = platform.architecture()[0]

if bit == '64bit':

    from arch64 import XYZ

    XYZ()

elif bit == '32bit':

    from arch32 import XYZ

    XYZ()

