from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import statistics
import json
import os

#initialize app
app = Flask(__name__)

#initialize db
base_directory = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_directory, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

#County model
class (County(db.Model)):
    id = db.Column(db.Integer, primary_key=True)
    zip = db.Column(db.String, unique=True, nullable=False)
    h_index = db.Column(db.Float, nullable=False)

    def __init__(self, zip, h_index):
        self.zip = zip
        self.h_index = h_index

#County Schema (excludes id from responses)
class CountySchema(ma.Schema):
    class Meta:
        fields = ('zip', 'h_index')

#import JSON Data
json_data = './happiness-index-seed-data.json'
with open(json_data) as file:
     counties = json.load(file)

#convert json key/values into instances of County and persist to db
for key in counties:
    count = County.query.filter_by(zip=key).count()
    if count > 0:
        break

    county = County(zip = key, h_index = counties[key])
    db.session.add(county)
    db.session.commit()
