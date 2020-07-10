# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 16:42:06 2020

@author: shrey.arora
"""
from googleapiclient import discovery
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd


cities = ['delhi','noida','gurugram','chandigarh','mumbai']
niches = ['food','restaurants','school','doctors','clinics','fashion','brands']
values = pd.DataFrame()

for city in cities:
    print(city)
    
    for niche in niches:
        print(niche)
        ##city = cities[0]
        ##niche =niches[0]
        
        
        url = "http://yellowpages.in/hyderabad/play-schools/905396227"
        try:
            page = urllib.request.urlopen(url)
        except:
            print("An error occured.")
        
        soup = BeautifulSoup(page, 'html.parser')
        #print(soup)
        
        
        
        company_names = soup.find_all('div',attrs={'class':"popularTitleTextBlock"})
        
        phone_numbers = soup.find_all('a',attrs={"class":'businessContact'})
        
        links = soup.find_all('div',attrs={"class":"eachPopularLink"})
        
        df = pd.DataFrame()
        for x in range(0,24):
            d={}
            name = company_names[x].getText()
            phone_num = phone_numbers[x].getText()[1:len(phone_numbers[x].getText())]
            try:
                email = links[x].find('a',attrs={"target":'_blank'})['href']
            except:
                email = ""
            d["name"]=name
            d["phone_num"]=phone_num
            d["email"]=email
            df = df.append(d,ignore_index=True)
            
            
                    
        
        
          
      