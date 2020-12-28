# Create your views here.
import os
from django.shortcuts import render, HttpResponse
import openpyxl
from pygeocoder import Geocoder
import pandas as pd
import numpy as np

from geopy.geocoders import Nominatim


def index(request):
    if "GET" == request.method:
        return render(request, 'addressLocator/index.html', {})
    else:
        nom = Nominatim(user_agent="addressLocator")
        
        excel_file = request.FILES["excel_file"]
        
        df = pd.read_excel(excel_file)
        
        df['Address'] = df['Address1']+", "+df['Address2']+", "+df['Address3']+", "+df['Address4']
        
        #df.head()
        df["Coordinates"] = df["Address"].apply(nom.geocode)
        
        df["Latitude"] = df["Coordinates"].apply(lambda x : x.latitude if x != None else None)      
        df["Longitude"] = df["Coordinates"].apply(lambda x : x.longitude if x != None else None)
     
        df.to_excel('updated_addresses.xls', sheet_name='Sheet1', index=False, engine='xlsxwriter')          
    
    return HttpResponse("Your File has been saved, do check inside your project folder!")