import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np

def getdata(url):
    r=requests.get(url)
    return r.text
if __name__ == '__main__':
    url="https://www.worldometers.info/coronavirus/"
    myhtml=getdata(url=url)

    soup = BeautifulSoup(myhtml, 'html.parser')
    #print(soup.prettify())

    table_body=soup.find('tbody')
    table_rows=table_body.find_all('tr')

    countries=[]
    cases=[]
    Today=[]
    Death=[]
    Recovred=[]

    for tr in table_rows:
        td = tr.find_all('td')
        countries.append(td[0])
        cases.append(td[1].text.replace(",",""))
        Today.append(td[2].text)
        Death.append(td[3].text)
        Recovred.append(td[5].text)
    #print(countries[8:])
    #print(cases[8:])
    #print(Today[8:])
    #print(Death[8:])
    #print(Recovred[8:])

    headers=["Countries","Total Cases","Today Cases","Death","Recovered"]
    today_cases=[]
    for i in range(len(Today)):
        today_cases.append(Today[i][1:])
    for i in range(len(Today)):
        if today_cases[i]== "":
            today_cases[i]=0
    for i in range(len(Recovred)):
        if Recovred[i] == "":
            Recovred[i] = 0
    print(len(Recovred))
    print(len(Recovred))
    print(cases)

