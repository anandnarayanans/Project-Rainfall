import pandas as pd
import requests
from bs4 import BeautifulSoup

SiteUrl = 'http://122.15.179.102/ARS/home/rainfall/'
startDate = '2022-04-01'
currentDate = '2022-04-07'
date_range = pd.date_range(startDate, currentDate)


def scrapRainfallData():
    for datevalue in date_range:
        formattedDate = datevalue.strftime('%Y-%m-%d')
        Url = f'{SiteUrl}{formattedDate}'
        print(f"Retreiving Rainfalldata for {formattedDate}\n")
        
        webScrapping(Url, formattedDate)


def webScrapping(url, date):

    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    data_iterator = iter(soup.find_all('td'))

    while True:
        try:
            Location = next(data_iterator).text
            ActualMM = next(data_iterator).text
            NormalMM = next(data_iterator).text
            next(data_iterator).text
            next(data_iterator).text
            next(data_iterator).text
            next(data_iterator).text
            print(f'{Location} : {ActualMM} : {NormalMM}')

        except Exception as errordaDei:
            print(f'{errordaDei}')
            break

        
def main():
    scrapRainfallData()

if __name__=="__main__":
    main()
