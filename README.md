# surfs_up
SQLite database weather analysis for opening a surf and shake shop on the Big Island.

## Overview
The purpose of this analysis was to help W. Avy, the primary investor in an upcoming "Surf and Ice Cream Shop" in Hawaii, with processing weather and temperature data into key figures. We wanted to show him some insights into the weather patterns around the months of June and December so that he would have enough statistical data to feel comfortable about openining the shop in such a location.
### Purpose
We used Pandas DataFrames, SQLite, and SQLAlchemy to create an engine from a SQLite file containing all the weather data we needed. We then processed the weather data using SQL queries on SQLite database in order to observe some key weather statistics for the months of June and December in Hawaii.


## Results

We imported the following dependencies in order to 




`engine = create_engine("sqlite:///hawaiii.sqlite")`

# reflect an existing database into a new model
`Base = automap_base()`
# reflect the tables
`Base.prepare(engine, reflect=True)`

# Save references to each table
`Measurement = Base.classes.measurement`
`Station = Base.classes.station`


## Summary

