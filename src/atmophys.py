"""
WORKING DOCUMENT
Below are predefined functions to be recalled for atmospheric physics. some can use scalar / Numpy arrays, others can't.
The functions SHOULD be appended with a suffix to determine it's use. I write these function (test versions) in the 

Certain functions accept scalars or NumPy arrays. passing multiple variables into a function will cause (I THINK) the output to match (e.g. a 2-D array if multiple temperatures and heights are passed to 'pressure'). had to look this one up... world wide web is awesome! (this is called broadcasting) 

Certain functions now (1.1.0) use vectorization, therefore they should not need loops such as in assignment_1 code on the stable branch.

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

R: float = 287.0 #J/kg*K
g: float = 9.81 #m/s**2

def scale_heightTc(Tc: Union[float, Iterable[float], np.ndarray]) -> np.ndarray:
    T_arr = np.asarray(Tc, dtype=float)
    if np.any(T_arr < -273.15):
        raise ValueError("Tempature(C) includes values below absolute zero (< -273.15 °C).")
    Tk = T_arr + 273.15
    H = (R*Tk)/g
    return H

def scale_heightTk(Tk: Union[float, Iterable[float], np.ndarray]) -> np.ndarray:
    T_arr = np.asarray(Tk, dtype=float)
    if np.any(T_arr < -273.15):
        raise ValueError("Tempature(K) includes values below absolute zero (< 0°K).")
    H = (R*Tk)/g
    return H

"""
should always return H as single float or np.array
"""

def pressureTc(
    Tc: Union[float, Iterable[float], np.ndarray],
    Z: Union[float, Iterable[float], np.ndarray],
    Ps: float = 101325.0,
    opt_unit,
) -> np.ndarray:
    H = scale_heightTc(Tc)
    Z_arr = np.asarray(Z, dtype=float)
    P = Ps*np.exp(-Z_arr / H[..., None] if np.ndim(H) else -Z_arr / H)
    if opt_unit == True:
        return print(f"{P} Paschals")
    else:
        return P


def pressureTk(
    Tk: Union[float, Iterable[float], np.ndarray],
    Z: Union[float, Iterable[float], np.ndarray],
    Ps: float = 101325.0,
    opt_unit,
) -> np.ndarray:
    H = scale_heightTk(Tk)
    Z_arr = np.asarray(Z, dtype=float)
    P = Ps*np.exp(-Z_arr / H[..., None] if np.ndim(H) else -Z_arr / H)
    if opt_unit == True:
        return print(f"{P} Paschals")
    else:
        return P