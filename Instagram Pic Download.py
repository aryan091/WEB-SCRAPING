import requests
from bs4 import BeautifulSoup

url="https://www.instagram.com/{}/"

def pic_downloader(username):
    full_url=url.format(username)
    r=requests.get(full_url)
    s=BeautifulSoup(r.text,"lxml")

    p=s.find("meta",property="og:image").attrs['content']

    with open(username+".jpg","wb") as pic:
        binary=requests.get(p).content
        pic.write(binary)


user_name=input("Please enter account name :")
data=pic_downloader(username=user_name)
print(data)
#"garima.__.singla"
