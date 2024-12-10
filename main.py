import requests
from bs4 import BeautifulSoup


def printing(theTitle, thePublicationDate, theAuthor, theP,  thePaywall):
    print("Title:", theTitle)
    print("Publication Date:", thePublicationDate)
    print("Author:", theAuthor)
    print("article:", theP)
    print("paywall:", thePaywall)

def toTextFile(theTitle, thePublicationDate, theAuthor, theP, thePaywall):
    file = open("title.txt", "w")
    file.write("Author: " + title + "\n")
    file.write("publication Date: " + publicationDate + "\n")
    file.write("Author: " + author + "\n")
    file.write("Article: " + p + "\n")
    file.write("Paywall: " + paywall + "\n")
    file.close()

link = "https://www.wired.com/story/luigi-mangione-arrested-uhc-shooting/"
x = requests.get(link)
soup = BeautifulSoup(x.content, "html.parser")

#getting text
title = soup.find('h1').text
publicationDate = soup.find('time').text
author = soup.find(class_="BaseWrap-sc-gjQpdd BaseText-ewhhUZ BaseLink-eNWuiM BylineLink-gEnFiw iUEiRd euNVPR jdMSdZ BDKtv byline__name-link button").text
p = soup.find('p').text
paywall = soup.find(class_="paywall").text

toTextFile(title, publicationDate, author, p, paywall)
printing(title, publicationDate, author, p, paywall)

