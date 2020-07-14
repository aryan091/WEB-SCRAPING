import requests
from bs4 import BeautifulSoup

"""
url="https://www.instagram.com/_aryan_0007/"

r=requests.get(url=url)
s=BeautifulSoup(r.text,"lxml")
print(s.prettify())
tag=s.find("meta",attrs={"name":"description"})
print(tag['content'])
"""
"""
import requests
from bs4 import BeautifulSoup

def getdata(url):
    r=requests.get(url)
    return r.text
if __name__ == '__main__':
    url="https://www.worldometers.info/coronavirus/"
    myhtml=getdata(url=url)

    soup = BeautifulSoup(myhtml, 'html.parser')

    p = soup.find("meta", property="og:image").attrs['content']

    with open("worldometers"+ ".jpg", "wb") as pic:
        binary = requests.get(p).content
        pic.write(binary)
"""
"""
url="https://www.google.com/search?q={}/"
r=requests.get(url=url)

s=BeautifulSoup(r.text,"html.parser")

ratings=[]
data=s.find_all("div",class_="Ap5OSd")
for i in data:
    d=i.text.split(".")
    ratings.append(d)
arr=[]
for i in ratings:
    arr+= i
first=arr[0]
print(first+"."+arr[1])
"""
url="https://www.covid19india.org/"
r=requests.get(url=url)

s=BeautifulSoup(r.text,"html.parser")
print(s.prettify())