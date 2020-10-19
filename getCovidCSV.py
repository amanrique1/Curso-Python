import urllib.request
from datetime import datetime
print("Start Program ... ")
try:
    print("Start Downloading file ... ")
    timenow = datetime.now()
    timenow_iso = timenow.strftime('%Y-%m-%dT%H:%M:%S') #Time ISO to second resolution
    url = 'https://opendata.arcgis.com/datasets/782122624f364fbdbd7e287b96c4a358_6.csv' #url
    output= f'data_RKI_{timenow_iso}.csv' # output's file name/ location
    urllib.request.urlretrieve(url, output)
    print(f"File {output} -- saved!")
except Exception as e:
    print("Downloading file error: " + str(e))