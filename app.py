from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/craigslist_app")

@app.route("/")
def index():
   planet = mongo.db.planet.find_one()
   return render_template('index.html', planet = planet)


@app.route("/scrape")
def scrape():
   planet = mongo.db.planet
   planet_data = scrape_mars.scrape()
   planet.update({}, planet_data, upsert=True)
   return redirect("http://localhost:5000/", code=302)

if __name__ == "__main__":
   app.run(debug=True)
