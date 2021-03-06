import pandas as pd
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import seaborn as sns

SiteUrl = 'http://122.15.179.102/ARS/home/rainfall/'
startDate = '2022-04-01'
currentDate = '2022-04-07'
date_range = pd.date_range(startDate, currentDate)


def scrapRainfallData():
    for datevalue in date_range:
        formattedDate = datevalue.strftime('%Y-%m-%d')
        Url = f'{SiteUrl}{formattedDate}'
        print(f"Retreiving Rainfalldata for {formattedDate}\n")
        dataframe = webScrapping(Url,formattedDate)
        print(dataframe)
        drawPlot(dataframe,formattedDate)


def webScrapping(url, date):

    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    data_iterator = iter(soup.find_all('td'))
    newdata = {}    
    districtList = []
    actualRainfall = []
    normalRainfall = []       
    
    while True:
        try:
       
            Location = next(data_iterator).text
            ActualMM = next(data_iterator).text
            NormalMM = next(data_iterator).text
            next(data_iterator).text
            next(data_iterator).text
            next(data_iterator).text
            next(data_iterator).text
            
            districtList.append(Location) 
            actualRainfall.append(float(str(ActualMM)))
            normalRainfall.append(float(str(NormalMM)))
            # print(f'{Location} : {ActualMM} : {NormalMM}')

        except Exception as errordaDei:
            print(f'{errordaDei}')
            break


    newdata['Location'] = districtList
    newdata['ActualRainfall'] = actualRainfall
    newdata['NormalRainfall'] = normalRainfall
    df = pd.DataFrame(newdata,columns=['Location','ActualRainfall','NormalRainfall'])    
    return df 

def drawPlot(df,date):
    sns.set(rc={'figure.facecolor':'cornflowerblue'})
    plt.style.use('fast')
    plt.plot(df.Location,df.NormalRainfall,linewidth=6,linestyle = '-')
    plt.plot(df.Location,df.ActualRainfall,'r--o',linewidth=4)
    plt.title(f'RainFall Data in mm for {date}')
    plt.legend(['Normal', 'Actual'])
    plt.xticks(rotation = 90.5)
    plt.show()
    
        
def main():
    scrapRainfallData()

if __name__=="__main__":
    main()
