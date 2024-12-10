import csv

from flask import Flask, render_template
import _csv

app = Flask(__name__)


articles = []
with open('data.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        articles.append(row)
@app.route('/')
def index():
    return render_template('index.html', data=articles)

if __name__ == '__main__':
    app.run(debug=True)
