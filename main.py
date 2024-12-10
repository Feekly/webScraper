import requests
from bs4 import BeautifulSoup

def toTextFile(theTitle, thePublicationDate, theAuthor, theP, thePaywall):
    file = open("data.csv", "w")
    #header row for dictReader
    file.write("title,date,author,p,paywall\n")
    file.write('"' + title + '",')
    file.write('"' + publicationDate + '",')
    file.write('"' + author + '",')
    file.write('"' + p + '",')
    file.write('"' + paywall + '"')
    file.close()

url = "https://www.wired.com/story/luigi-mangione-arrested-uhc-shooting/"
x = requests.get(url)
soup = BeautifulSoup(x.content, "html.parser")

#getting text
title = soup.find('h1').text
publicationDate = soup.find('time').text
author = soup.find(class_="BaseWrap-sc-gjQpdd BaseText-ewhhUZ BaseLink-eNWuiM BylineLink-gEnFiw iUEiRd euNVPR jdMSdZ BDKtv byline__name-link button").text
p = soup.find('p').text
paywall = soup.find(class_="paywall").text

toTextFile(title, publicationDate, author, p, paywall)

