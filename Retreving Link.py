import requests
from bs4 import BeautifulSoup
def getData(url):
    r = requests.get(url=url)
    return r.text
if __name__ == '__main__':

    url="https://www.mycodingzone.net/blog/english"
    mthtml=getData(url)
    soup=BeautifulSoup(mthtml,'html.parser')
    print("-"*100)
    for links in soup.find_all('a'):
        link=links.get('href')
        if link[0:3]=="../" and link!="#":
            print("https://www.mycodingzone.net/"+link[2:])
        elif link[0] == "/" and link!="#":
            print("https://www.mycodingzone.net/" + link)
        elif link!="#":
            print(link)
