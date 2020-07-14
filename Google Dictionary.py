import requests
from bs4 import BeautifulSoup

def dictionary(word,lan):
    url="https://www.google.com/search?q=meaning+of+"+word+"+in+"+lan+"&oq=meaning+of+moron+&aqs=chrome.1.69i57j0l7.16113j1j8&sourceid=chrome&ie=UTF-8"
    r=requests.get(url)
    s=BeautifulSoup(r.text,"lxml")
    w=s.find("div",class_="BNeawe iBp4i AP7Wnd")
    return w.text.strip()


if __name__ == '__main__':
    lan = input("Please enter language in which you want to translate : ")
    word = input("Please enter word : ")
    print(dictionary(word=word,lan=lan))