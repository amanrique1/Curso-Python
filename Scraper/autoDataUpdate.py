#Execute the tasks with 5min delay(300000ms)
#pm2 start autoDataUpdate.py --name covid19-5minInt restart-delay 300000
#pm2 l to see the task log
import requests, datetime
from bs4 import BeautifulSoup #To install: pip3 install beautifulsoup4
url = "https://www.worldometers.info/coronavirus/"
req = requests.get(url)
bsObj = BeautifulSoup(req.text, "html.parser")
data = bsObj.find_all("div",class_ = "maincounter-number")
NumTotalCase = data[0].text.strip().replace(',', '')
NumDeaths = data[1].text.strip().replace(',', '')
NumRecovered = data[2].text.strip().replace(',', '')
TimeNow = datetime.datetime.now()
with open('world_corona_case.csv','a') as fd:
    fd.write(f"{TimeNow},{NumTotalCase},{NumDeaths},{NumRecovered};")
print(f"Successfully store COVID-19 data at {TimeNow}")