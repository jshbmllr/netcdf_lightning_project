import requests
import pandas as pd
import xarray as xr

url = 'https://noaa-goes18.s3.amazonaws.com/GLM-L2-LCFA/2023/001/00/OR_GLM-L2-LCFA_G18_s20230010000000_e20230010000200_c20230010000213.nc'
r = requests.get(url, allow_redirects=True)

with open ('dl/lightning_data.nc', 'wb') as f:
    f.write(r.content)