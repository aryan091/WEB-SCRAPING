import requests
from bs4 import BeautifulSoup

def weatherststus(cityname):
    url = "https://www.google.com/search?q="+cityname+"+" "weather/"
    r=requests.get(url=url)
    s=BeautifulSoup(r.text,'html.parser')
    w=s.find_all("div",class_="BNeawe iBp4i AP7Wnd")
    data=list(w)
    return data[1].text.strip()

if __name__ == '__main__':
    cityname = input("Please enter city name :")
    print(weatherststus(cityname=cityname))