from flask import Flask
from flask import render_template as rt
import requests, json, warnings
response = requests.get("https://api.openbrewerydb.org/v1/breweries")

data = json.loads(response.text)

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return rt("home.html", user="Ethan Harrison")

@app.route("/breweries")
def breweries():
    return rt("breweries.html", content = data)

@app.route("/beer_types")
def beer_types():
    return rt("beer_types.html", user="Ethan Harrison")
@app.route("/about")
def about():
    return rt("about.html", user="Ethan Harrison")

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)

