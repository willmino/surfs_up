# import flask dependencies

import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


# this line of code allows us to accecss the sqlite database, and it requires the location of the database (file name within the folder)
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect the database into our classes

Base = automap_base()

#add following code to reflect the database. The engine will be reflected on the Base. The Base is an instance created that does not yet have any meaning to us, unless we reflect it.
Base.prepare(engine, reflect=True)

# assign variables for the table columns, so that its easier to use in the SQLite query code
# this is saving our table references
Measurement = Base.classes.measurement
Station = Base.classes.station

#Finally, create a session link from python to our database
session = Session(engine)


# After connecting this python file to the SQLite database, all of the code above, 
# We now create a new instance of the flask app

app = Flask(__name__)


# note:
# If we wanted to import our app.py file into another Python file named example.py, the variable __name__ would be set to example. Which would be a modification to the line of code directly above.

# first, define the starting point, known as the ROOT,  this line of code is the root = @app.route('/')
@app.route('/')


def welcome():
    return(

    '''

    Welcome to the Climate Analysis API!

    Available Routes:

    /api/v1.0/precipitation

    /api/v1.0/stations

    /api/v1.0/tobs

    /api/v1.0/temp/start/end

    ''')

#create the precipitation route
@app.route("/api/v1.0/precipitation")


def precipitation():

    # this line of code will obtain the date that is one year before the most recent date in the database
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()

    precip = {date: prcp for date, prcp in precipitation}

    return jsonify(precip)


@app.route("/api/v1.0/stations")

def stations():

    results = session.query(Station.station).all()

    stations = list(np.ravel(results))

    return jsonify(stations=stations)

#create the temperature observation (tobs) [actually named [temp_monthly; in this module] route
@app.route("/api/v1.0/tobs")

def temp_monthly():

    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()

    temps = list(np.ravel(results))

    return jsonify(temps=temps)

#create the temp/start/end route

@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

# next, create a function called stats() to put our code in it.

# we need to add paramters to the stats() function. Start parameter and an end parameter. For now, set both parameters to None

def stats(start=None, end=None):

    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        
        temps = list(np.ravel(results))

        return jsonify(temps)

    results = session.query(*sel).\
            filter(Measurement.date >= start).\
            filter(Measurement.date <= end).all()

    temps = list(np.ravel(results))


    return jsonify(temps)

