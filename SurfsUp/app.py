from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
import numpy as np
import datetime as dt 
import pandas as pd


engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(autoload_with=engine)

Station = Base.classes.station
Measurement = Base.classes.measurement

app = Flask(__name__)

@app.route("/")
def welcome():
    """List of all the available routes"""
    return(
        f"Available Routes for Hawaii Weather:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )   
    
@app.route("/api/v1.0/precipitation")
def precipitation():
    session= Session(engine)
    """Return a list of precipitation(prcp) and date(date) data"""
    results = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= '2016-08-23').all()
    session.close()
    
    precipitation_list = {date:prcp for date,prcp in results}
    
    return jsonify(precipitation_list)

@app.route("/api/v1.0/stations")
def station():
    session= Session(engine)
    """Return a list of Stations from the dataset"""
    results = session.query(Station.station).all()
    session.close()
    
    station_names = list(np.ravel(results))
    
    return jsonify(station_names)

@app.route("/api/v1.0/tobs")
def temperature():
    session= Session(engine)
    """Return a list of Temperature and dates data"""
    results = session.query(Measurement.date,Measurement.tobs).\
        filter(func.strftime(Measurement.date)>= '2016-08-23', Measurement.station=='USC00519281').all()
    session.close()
    
    active_station = []
    for date, tobs in results:
        active = {}
        active["date"]= date
        active["tobs"]= tobs
        active_station.append(active)
    return jsonify(active_station)   


@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    session= Session(engine)    
    """Return TMIN, TAVG, TMAX for start and start-end date"""
    start = dt.datetime.strptime(start, '%Y-%m-%d')
        
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    if not end:        
        # calculate TMIN, TAVG, TMAX for dates greater than start        
        results = session.query(*sel).filter(Measurement.date >= start).all()        
             
        temps = list(np.ravel(results))        
        return jsonify(temps)
    end = dt.datetime.strptime(end,'%Y-%m-%d')
    # calculate TMIN, TAVG, TMAX with start and stop    
    results = session.query(*sel).filter(Measurement.date >= start).filter(Measurement.date <= end).all()    
        
    temps = list(np.ravel(results))    
    return jsonify(temps=temps)
     

    
if __name__=='__main__':
    app.run(debug=True)