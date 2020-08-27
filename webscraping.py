# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 23:40:15 2020

@author: Tejas
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd

source = requests.get('https://www.bikewale.com/vespa-bikes/vxl-125/images/').text
soup = BeautifulSoup(source, 'html.parser')


vehicle = []
for bikes_detail in soup.findAll('img', attrs = {'class':'lazy'}) :
    vehicle.append(bikes_detail.get('src'))
print(vehicle)

df = pd.DataFrame()
df['Vehicle'] = vehicle
df

bike_name =['marutisuzuki-cars','hyundai-cars','mahindra-cars','tata-cars','toyota-cars','renault-cars','honda-cars','mg-cars','ford-cars','kia-cars','volkswagen-cars','mercedesbenz-cars','skoda-cars','audi-cars','jeep-cars','datsun-cars','landrover-cars','fiat-cars']
