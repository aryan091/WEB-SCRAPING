import requests
from bs4 import BeautifulSoup

def realtimecurrency(cur):
    url="https://www.google.com/search?q=latest+value+of+"+cur+"&oq=latest+value+of+"+cur+"&aqs=chrome..69i57.14123j0j8&sourceid=chrome&ie=UTF-8"
    r=requests.get(url)
    s=BeautifulSoup(r.text,"lxml")
    price=s.find("div",class_="BNeawe iBp4i AP7Wnd")
    return price.text.strip()

if __name__ == '__main__':
    cur = input("Please enter e-currency name for conversion : ")
    print(realtimecurrency(cur=cur))