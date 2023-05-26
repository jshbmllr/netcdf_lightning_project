import requests
import pandas as pd
import xarray as xr

url = 'https://noaa-goes18.s3.amazonaws.com/GLM-L2-LCFA/2023/001/00/OR_GLM-L2-LCFA_G18_s20230010000000_e20230010000200_c20230010000213.nc'
r = requests.get(url, allow_redirects=True)

with open ('dl/lightning_data.nc', 'wb') as f:
    f.write(r.content)

data = xr.open_dataset('dl/lightning_data.nc')
# print(data['event_lon'].values)
# print(data['group_lat'].values)
# print(data['event_time_offset'].values)
# subset = data.sel(event_lon=-102.80444895, event_lat=20.977652, method='nearest')
# print(subset)

