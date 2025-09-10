"""
WORKING DOCUMENT (1.0.1)
Below are predefined functions to be recalled for atmospheric physics. some can use scalar / Numpy arrays, others can't.
The functions SHOULD be appended with a suffix to specify certain uses (_k or _c suffix on scale height for celcius or kelvin). I copy these functions from stable code in Jupyter. Complex versions can be found in the test branch of this repo. branches will be merged as code becomes stable. 

############################
### IMPORTING TO JUPYTER ###
############################
!!MUST IMPORT NUMPY FIRST!!

to avoid a full clone of the repo, download just this file:

import sys, pathlib, urllib.request
url = "https://raw.githubusercontent.com/charkeyser/Climatology-Coursework-undergrad-/main/src/atmophys.py"
urllib.request.urlretrieve(url, "atmophys.py")
sys.path.append(str(pathlib.Path.cwd()))
from atmophys import <functions you want, separated by commas>

############################

list of basic equations:
scale height = R*T/g = H
pressure = Ps*np.exp(-z / H) = P

List of basic variables:
R = 287 J/kg*K (universal gas constant assuming dry air)
g = 9.81 m/s**2 (gravitational constant on earth)
Tc = temperature in celsius 
Tk = absolute temperature in kelvin
Z = height in meters ASL
Ps = 101325 Pa (standard pressure at 0 ft ASL)

"""


from __future__ import annotations
from typing import Iterable, Union
import numpy as np

def scale_height_c(T):
    R = 287 #J/kg*K (universal gas constant)
    g = 9.81 #m/s**2
    H = R*(T+273.15)/g
    return H

def scale_height_k(T):
    R = 287 #J/kg*K (universal gas constant)
    g = 9.81 #m/s**2
    H = R*T/g
    return H

def pressure(T, Z, H, opt_unit):
    Ps = 101325 #Pa
    P = Ps*np.exp(-Z/H)
    if opt_unit == True:
        return print(f"{P} Paschals")
    else:
        return P

"""
should always return H or P as single float or 1-D array if multiple values are passed per variable (E.G. multiple Z values)
"""

