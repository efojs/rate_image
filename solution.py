import numpy as np
import pandas as pd
import rawpy


def get_max(array_type):
    return 2**(2**array_type.num)-1

def extend_range_to_max(flat, max):
    flat[0] = 0
    flat[1] = max
    return flat

def rate_image(raw_image, max=None):
    flat = raw_image[::2,::2].flatten(order='C')
    if not max:
        max = get_max(flat.dtype)
    flat = extend_range_to_max(flat, max)
    skew = pd.Series(flat).skew()
    if skew < -1:
        return 'Overlight'
    elif skew > 1:
        return 'Underlight'
    else:
        return 'Normal'

files = [
    'DSC_0008.NEF',
    'DSC_0009.NEF',
    'DSC_0010.NEF',
    'DSC_0011.NEF',
    'DSC_0012.NEF',
]

for file_name in files:
    with rawpy.imread(file_name) as raw:
        print(file_name, rate_image(raw.raw_image, max=4095))
