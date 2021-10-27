import numpy as np
import pandas as pd
import rawpy

def rate_image(raw_image):
    flat = raw_image[::2,::2].flatten(order='C')
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
        print(file_name, rate_image(raw.raw_image))
