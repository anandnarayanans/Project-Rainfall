from pandas.core.indexes.datetimes import date_range
import requests
import pandas as pd
from bs4 import BeautifulSoup

startDate = '2021-01-01'
currentDate = '2021-11-07'
rainfallDate = '2021-11-07'
date_range = pd.date_range(startDate, currentDate)


def scrapRainfallData():
    for datevalue in date_range:
        formattedDate = datevalue.strftime('%Y-%m-%d')
        Url =  f'{formattedDate}'
        print(f"Retreiving data for {formattedDate}")
        webScrapping(Url)


def webScrapping(url,date):

    URL =  f'http://122.15.179.102/ARS/home/rainfall/{rainfallDate}'
    r= requests.get(URL)


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

            except Exception as err:
                print(err)          

            scrapRainfallData()
