import requests
from bs4 import BeautifulSoup



def moviesrating(moviename):
    url = "https://www.google.com/search?q="+moviename+"/"
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
    return first+"."+arr[1]

if __name__ == '__main__':
    moviename=input("Please enter movie name for view their ratings : ")
    movie_rating=moviesrating(moviename)
    print("MOVIE RATINGS : ",moviename)
    print(movie_rating)