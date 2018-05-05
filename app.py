"""

<Chan Feng> 2018-05-04 Rutgers Data Science Boot Camp Assignment Week 13. Web scrapping, MongoDB and Flask

This file provide web app functionality

"""

from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from mars_scrapper import get_mission_to_mars_info

app = Flask(__name__)
mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('index.html', data=mongo.db.mission_to_mars.find_one())

@app.route('/scrape')
def scrape():
    mongo.db.mission_to_mars.update(
        {},
        get_mission_to_mars_info(),
        upsert=True
    )
    return redirect('http://localhost:5000/', code=302)

if __name__ == '__main__':
    app.run()