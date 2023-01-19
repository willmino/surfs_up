# surfs_up
SQLite database weather analysis for opening a surf and shake shop on the Big Island.

## Overview
The purpose of this analysis was to help W. Avy, the primary investor in an upcoming "Surf and Ice Cream Shop" in Hawaii, with processing weather and temperature data into key figures. We wanted to show him some insights into the weather patterns around the months of June and December so that he would have enough statistical data to feel comfortable about openining the shop in such a location.
### Purpose
We used Pandas DataFrames, SQLite, and SQLAlchemy to create an engine from a SQLite file containing all the weather data we needed. We then processed the weather data using SQL queries on SQLite database in order to observe some key weather statistics for the months of June and December in Hawaii.


## Results

We imported the following dependencies in order to connect python to the SQLite database file `hawaii.sqlite`.

![dependencies](https://github.com/willmino/surfs_up/blob/main/dependencies/dependencies.png)

We then created the engine and set `create_engine()` SQLAlchemy function the parameter to the name of the SQLite database. A Base class was declared using the SQLalchemy `automap_base()` function. This Base class was necessary because we first needed to create an instance of the database. Then, we could reflect this instance (Base) so that the tables of the database could be iterated through using our python code and SQLAlchemy queries. References were assigned to the variable `Measurement` and `Station`. We would then reference these variables as the tables through out our SQLite queries. The code block was summarized below:

`engine = create_engine("sqlite:///hawaii.sqlite")`

`# reflect an existing database into a new model`

`Base = automap_base()`

`# reflect the tables`

`Base.prepare(engine, reflect=True)`

`# Save references to each table`

`Measurement = Base.classes.measurement`

`Station = Base.classes.station`

To view the column names and specifications from each table we initialized the inspector by using:

`inspector = inspect(enginge)`

The `Measurement_columns` variable was set equal to the `inspector` chained to the `get_columns()` function. We passed the name of each table in the `get_columns()`. Each row of the `Measurement_columns` variable was then printed as a for loop. We could see each row contained the name and other specifications for each column.

`Measurement_columns = inspector.get_columns('Measurement')`

`for row in Measurement_columns:`

&nbsp;&nbsp;&nbsp;&nbsp;`print(row)`

Before performing the queries, we needed to create a session engine:

`session = Session(engine)`

Now that we could view the database within python, we felt comfortable enough to start performing the SQLite queries.

We imported the `extract` module from SQLalchemy. Our first query selected the temperature observations `tobs` column from the `Measurement` table. We then filtered the selection on the `date` column and chained it to the `.like()` function, passing the string `'%-06-%` through it. This allowed the query to filter the `date` column and only return `tobs` data that had the string `'-06-'` in it, or temperatures only collected in the month of June. For example, the date format in the `Measurement Column` was `YYYY-MM-DD` and the date `June 1st, 2010` would appear as  `2010-06-01`. So all the dates that looked like `XXXX-06-XX` would be returned. We then stored the results of the query in a list using the `list()` function. The list was then stored in a Pandas DataFrame using the `pd.DataFrame()` function The code for this query was listed below:

`from sqlalchemy import extract`

`June_Temps = session.query(Measurement.tobs).\`

&nbsp;&nbsp;&nbsp;&nbsp;`filter(Measurement.date.like('%-06-%'))`

`June_temperatures = list(June_Temps)`

`june_df = pd.DataFrame(June_temperatures,columns = ["June Temps"])`

Finally, the summary statistics table for the temperatures in the month of June was generated on the `june_df` dataframe using the `.describe()` function. The final line of code was:

`june_df.describe()`

The resulting summary statistics table was visualized below:

![June_Temps](https://github.com/willmino/surfs_up/blob/main/images/June_Temperatures.png)

The same query was applied to find the temperatures, `tobs`, from the `Measurement` table for the month of December.

`December_Temps = session.query(Measurement.tobs).\`

&nbsp;&nbsp;&nbsp;&nbsp;`filter(Measurement.date.like('%-12-%'))`

`december_temperatures = list(December_Temps)`

`december_df = pd.DataFrame(december_temperatures,columns = ["June Temps"])`

`december_df.describe()`

The resulting summary statistics table was visualized below:

![December_Temps](https://github.com/willmino/surfs_up/blob/main/images/December_Temperatures.png)










## Summary

