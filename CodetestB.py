import urllib2
import xml.etree.ElementTree as ET
import pandas as pd

tree = ET.ElementTree(file=urllib2.urlopen('http://syndication.enterprise.websiteidx.com/feeds/BoojCodeTest.xml'))
root = tree.getroot()
Listings=pd.DataFrame(columns=['MlsId', 'MlsName', 'DateListed', 'StreetAddress', 'Price', 'Bedrooms', 'Bathrooms', 'Appliances', 'Rooms', 'Description'])

for i, Listing in enumerate(root.findall('Listing')):        
    if Listing.find('ListingDetails').find('DateListed').text[:4]=='2016' and ' and ' in Listing.find('BasicDetails').find('Description').text:       
        try:
            misid_= Listing.find('ListingDetails').find('MlsId').text 
        except :
            misid_=''
        try:        
            MlsName_=Listing.find('ListingDetails').find('MlsName').text
        except :
            MlsName=''        
        try:   
            DateListed=Listing.find('ListingDetails').find('DateListed').text
        except :
            DateListed=''
        try:    
            StreetAddress=Listing.find('Location').find('StreetAddress').text       
        except :
            StreetAddress=''           
        try:
            Price=Listing.find('ListingDetails').find('Price').text
        except :
            Price=''            
        try:
            Bedrooms= Listing.find('BasicDetails').find('Bedrooms').text
        except :    
            Bedrooms=''
        try: 
            Bathrooms=Listing.find('BasicDetails').find('Bathrooms').text
        except :
            Bathrooms=''    
        try:    
            Appliances=''
            for appl in Listing.find('RichDetails').find('Appliances').findall('Appliance'):
                Appliances= Appliances+','+ appl.text
            Appliances=Appliances[1:]
        except :
            Appliances=''       
        try:  
            Room=''  
            for rm  in Listing.find('RichDetails').find('Rooms').findall('Room'): 
                Room = Room+','+ rm.text 
            Room=Room[1:]            
        except :
            Room=''        
        try:    
            Description = Listing.find('BasicDetails').find('Description').text[:200] 
        except :
            Description=''        
        Listings.loc[i] = [misid_,MlsName_,DateListed,StreetAddress,Price,Bedrooms,Bathrooms,Appliances,Room,Description]

Listings['DateListed'] =pd.to_datetime(Listings['DateListed'])
Listings=Listings.sort_values(by='DateListed')
Listings.to_csv(r'C:\Users\mandar\Desktop\KaggleData\CodeTestBooj\listings2016.csv',index=False)        