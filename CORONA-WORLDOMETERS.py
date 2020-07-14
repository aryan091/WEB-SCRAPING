import requests
from bs4 import BeautifulSoup

def getdata(url):
    r=requests.get(url)
    return r.text
if __name__ == '__main__':
    url="https://www.worldometers.info/coronavirus/"
    myhtml=getdata(url=url)

    soup = BeautifulSoup(myhtml, 'html.parser')

    details = soup.find_all("div",class_="maincounter-number")
    print("       WORLDOMETER                    ")
    print("TOTAL CASES :",details[0].text.strip())
    print("TOTAL DEATHS :",details[1].text.strip())
    print("TOTAL RECOVERED :",details[2].text.strip())
