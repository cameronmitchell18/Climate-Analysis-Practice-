from flask import Flask, jsonify
import pandas as pd
import numpy as np 
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# app = Flask(__name__)

# @app.route('/')

# # def hello_world():
# #     return 'Hello World'

engine = create_engine("sqlite:///hawaii.sqlite")

Base = automap_base()

Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement

Station = Base.classes.station

session = Session(engine)

app = Flask(__name__)

@app.route("/")

def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:\n
    /api/v1.0/precipitation\n
    /api/v1.0/stations\n
    /api/v1.0/tobs\n
    /api/v1.0/temp/start/end
    ''')