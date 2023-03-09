# sqlalchemy_challenge

CONTAINS:

Folder name= "SurfsUp" which includes:

1.Resources folder

2.Climate_starter.ipyb

3.app.py

In Climate_starter: Designed query for different data analysis

Most active station = "USC00519281" 

Designed query for min, max, and average temperatures for this active station.

Saved query results to a Pandas DataFrame as precipitation_df and active_df.

Precipitation analysis graph -

![image](https://user-images.githubusercontent.com/119129801/223959962-c828bb20-5293-4981-b88b-e862a29a5705.png)

Station analysis histogram-

![image](https://user-images.githubusercontent.com/119129801/223960203-47b25ad5-3c8e-4b96-a7ab-b9fe446fc68a.png)

In app.py:

Creating and binding the session between the python app and database

Designed Flask API using query from climate_starter.ipynb file by importing flask and creating routes.

Jsonify representation is returned.(Using Flask Jsonify function to convert API into valid Json response.)

Routes created- precipitation, stations, tobs, start route and start/end route.

For preciptation route : Returns JSON dictionary of date as the key and the value as the precipitation(last 12 months of data).

For Station route: Returns JSON list of Station.

For Tobs route: Returns JSON list of temperature observations for the previous year.

For Start date route: Return a JSON list of TMIN, TAVG, and TMAX for a specified start date.

For Start and End date route: Return a JSON list of TMIN, TAVG, and TMAX for dates from the start date to the end date, inclusive.


