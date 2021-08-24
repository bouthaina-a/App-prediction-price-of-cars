import pandas as pd
import numpy as np
import time
import sys
import requests
from bs4 import BeautifulSoup as bs

brands = {
 'Marque': 0,
 'Alfa Romeo': 1,
 'Aston Martin': 2,
 'Audi': 3,
 'Bentley': 4,
 'BMW': 5,
 'BYD': 6,
 'Cadillac': 7,
 'Changhe': 8,
 'Chery': 9,
 'Chevrolet': 10,
 'Chrysler': 11,
 'Citroen': 12,
 'Dacia': 13,
 'Daihatsu': 14,
 'Dodge': 15,
 'Ferrari': 16,
 'Fiat': 17,
 'Ford': 18,
 'Foton': 19,
 'Geely': 20,
 'GMC': 21,
 'Honda': 22,
 'Hummer': 23,
 'Hyundai': 24,
 'Infiniti': 25,
 'Isuzu': 26,
 'Iveco': 27,
 'Jaguar': 28,
 'Jeep': 29,
 'Kia': 30,
 'Lamborghini': 31,
 'lancia': 32,
 'Land Rover': 33,
 'Lexus': 34,
 'Lincoln': 35,
 'Mahindra': 36,
 'Man': 37,
 'Maserati': 38,
 'Masey Ferguson': 39,
 'Mazda': 40,
 'Mercedes-Benz': 41,
 'mini': 42,
 'Mitsubishi': 43,
 'Nissan': 44,
 'Opel': 45,
 'Peugeot': 46,
 'Pontiac': 47,
 'Porsche': 48,
 'Renault': 49,
 'Seat': 50,
 'Skoda': 51,
 'Smart': 52,
 'Ssangyong': 53,
 'Subaru': 54,
 'Suzuki': 55,
 'Toyota': 56,
 'UFO': 57,
 'Volkswagen': 58,
 'Volvo': 59,
 'Zotye': 60
 }

def getPrice(price):
    price = price.text
    if price == "Prix non specifié":
        price = np.nan
    else:
        price = price[0:-3]
        if len(price) <= 7 and len(price) >=5 :
            priceFinal = price[:price.index(' ')]
            priceFinal += price[price.index(' ')+1:]
            price = int(priceFinal)
        else:
            price = np.nan
    return price

def url(ville, price_min, price_max, brand, model):
    if ville == None:
        ville = "maroc"
    price_min = "&spr="+str(price_min)
    price_max = "&mpr="+str(price_max)
    model = "&mo="+model.replace(' ', '_').lower()
    brand = "&cb="+str(brands[brand])
    # get url
    url = "https://www.avito.ma/fr/"+ville.lower()+"/voitures-%C3%A0_vendre?"+price_min+price_max+brand+model
    return url

def cars(ville, price_min, price_max, brand, model):
    if ville == None:
        ville = "maroc"
    price_min = "&spr="+str(price_min)
    price_max = "&mpr="+str(price_max)
    model = "&mo="+model.lower()
    brand = "&cb="+str(brands[brand])
    # get url
    url = "https://www.avito.ma/fr/"+ville.lower()+"/voitures-%C3%A0_vendre?"+price_min+price_max+brand+model
    # get page
    page = requests.get(url)
    # page form html
    container = bs(page.content,'html.parser')
    #find paragraphe using tagname and class
    
    container = container.find("div",{"class":"sc-1nre5ec-0 fdVHEH listing"})
    price_container = container.findAll("span",{"class":"sc-1x0vz2r-0 eCRZyT oan6tk-16 llzUZv"})
    desc_container = container.findAll("span",{"class":"oan6tk-18 gJxgUN"})
    hrefs = container.findAll("a")
    dd = list()
    for price, desc, a in zip(price_container, desc_container, hrefs):
        try:
            p = getPrice(price)
            d = desc.text
            if type(p) != int:
                continue
            else:
                dd.append((d, p, a.get("href"), image_url(a.get("href"))))
            if len(dd) == 3:
                break
        except:
            continue
    return dd


def image_url(url):
    try:
        page = requests.get(url)
        container = bs(page.content,'html.parser')
        container = container.find("div",{"class":"sc-1g3sn3w-12 isfwtH"})

        return container.picture.img['src']
    except:
        return ''