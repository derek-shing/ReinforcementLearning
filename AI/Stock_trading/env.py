#Get data
#define state
#next_step
#Calculate value
#Calculate return
import requests
import pandas as pd

class Market():

    def get_data(self):

        #data provider URL: https://api.tiingo.com/

        token="bd6c49fc0c3f94a9c91d1f209cf901d9373169b1"
        headers = {
        'Content-Type': 'application/json',
        'Authorization' : 'Token '+token
        }
        url="https://api.tiingo.com/tiingo/daily/AAPL/prices?startDate=2012-1-1&endDate=2018-1-1 "

        requestResponse = requests.get(url,headers=headers)
        df = pd.DataFrame(requestResponse.json())
        print(df.head())




m = Market()
m.get_data()
