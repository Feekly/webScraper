import csv
from flask import Flask, render_template, request

app = Flask(__name__)
def scrapeUrl(url):
    import requests
    from bs4 import BeautifulSoup

    x = requests.get(url)
    soup = BeautifulSoup(x.content, "html.parser")

    #getting text
    title = soup.find('h1').text
    publicationDate = soup.find('time').text
    author = soup.find(class_="BaseWrap-sc-gjQpdd BaseText-ewhhUZ BaseLink-eNWuiM BylineLink-gEnFiw iUEiRd euNVPR jdMSdZ BDKtv byline__name-link button").text
    p = soup.find('p').text
    paywall = soup.find(class_="paywall").text
    return {
        'title': title,
        'date': publicationDate,
        'author': author,
        'p': p,
        'paywall': paywall
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.form.get('url')
    if not url:
        return "No URL provided"
    data = scrapeUrl(url)
    return render_template('results.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
