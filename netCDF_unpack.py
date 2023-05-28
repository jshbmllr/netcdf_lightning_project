import requests
import pandas as pd
import xarray as xr

# Thank you so much for the opportunity! This was a fun challenge for me. Looking forward to discussing it soon!
# A URL to paste into the terminal for testing:
# https://noaa-goes18.s3.amazonaws.com/GLM-L2-LCFA/2023/001/00/OR_GLM-L2-LCFA_G18_s20230010000000_e20230010000200_c20230010000213.nc

def import_data(url: str):

    res = requests.get(url, allow_redirects=True)
    if res.status_code == 200:
# I suspect there is a way to build the xarray from the binary in memory, but I couldn't get there. I would also potentially add an option to write to a file
# as well as allow user to specify file name. Would be useful to append a numbers if the file existed to avoid rewrites.
        with open ('dl/lightning_data.nc', 'wb') as f:
            f.write(res.content)
        dataset = xr.open_dataset('dl/lightning_data.nc')
        
        return dataset

    else:
        print('Error:', res.status_code)
        return None
    
# I'm not familiar with xarray enough to extract the extract data_array I was looking for (that would be a 3D array of events with lat lon and time as the dims)
# so I fell back to converting to pandas DataFrame, which I've worked with pretty extensively. I also elected to just sort the data on import based on lat with the assumption the user will
# always be searching for events in a given lat/lon bounded box. Specifically, this allows me to use searchsorted() to hopefully speed up the searching.
# sortedsearch() runs a binary search on lat for the bounds to limit the values that will be iterated over. I'm sure there's a cleaner way to get where I wanted,
# but I'm familiar with  the method and hammer, nail, etc.

def sort_into_frame(data):
    event_frame = pd.DataFrame({'lat': data['event_lat'].values, 
                                'lon': data['event_lon'].values, 
                                'time': data['event_time_offset'].values, 
                                'event_id' : data['event_id'].values}).sort_values('lat')
    return event_frame

def search_frame(df: pd.DataFrame, min_lat: float, max_lat: float, min_lon: float, max_lon: float):
    lower_bound = df['lat'].searchsorted(min_lat)
    upper_bound = df['lat'].searchsorted(max_lat, side='right')

    requested_frame = df[lower_bound:upper_bound+1][(df['lon'] >= min_lon) & (df['lon'] <= max_lon)]

    return requested_frame


def main():
    url = str(input('Please provide the url of the lightning data you would like to download: '))
    
    print('Downloading...')
    data = import_data(url)
    print('Formatting...')
    sorted_data = sort_into_frame(data)
    print('Ready!')
    print(sorted_data)

    first_loop = True

    # The loop is pretty crude and would need some error handling to make sure the url was a url, if the import_data() returned None, etc.
    while True:
        query = 'Would you like to see a subset of the data (y/n)? ' if first_loop else 'Would you like to see another subset of the data (y/n)? '
        first_loop = False
        user_input = str(input(query))
        if user_input == 'y':
            print('Please enter the latitude and longitude bounds for the desired data:')
            lat_min = float(input("Minimum latitude: "))
            lat_max = float(input("Maximum latitude: "))
            lon_min = float(input("Minimum longitude: "))
            lon_max = float(input("Maximum longitude: "))
            req = search_frame(sorted_data, lat_min, lat_max, lon_min, lon_max)
            print(req)
        if user_input == 'n':
            break
    
main()
