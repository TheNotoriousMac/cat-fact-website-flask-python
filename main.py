from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
import requests

app = Flask(__name__)
Bootstrap5(app)

def get_random_cat_fact():
    url = 'https://catfact.ninja/fact'
    response = requests.get(url)
    cat_fact_text = response.json()['fact']
    return cat_fact_text

@app.route('/')
def home():
    cat_fact = get_random_cat_fact()
    return render_template('index.html', cat_fact=cat_fact)


if __name__ == '__main__':
    app.run(debug=True)