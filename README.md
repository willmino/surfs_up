# surfs_up

## Overview
The purpose of this analysis was to help W. Avy, the primary investor in an upcoming "Surf and Ice Cream Shop" in Hawaii, with processing weather and temperature data into key figures. We wanted to show him some insights into the weather patterns around the months of June and December so that he would have enough statistical data to feel comfortable about openining the shop in such a location.
### Purpose
We used Pandas DataFrames, SQLite, and SQLAlchemy to create an engine from a SQLite file containing all the weather data we needed. We then processed the weather data using SQL queries on the SQLite database in order to observe some key weather statistics for the months of June and December in Hawaii.


## Results

We imported the following dependencies in order to connect python to the SQLite database file named `hawaii.sqlite`.

![dependencies](https://github.com/willmino/surfs_up/blob/main/dependencies/dependencies.png)

We then created the engine and set the `create_engine()` SQLAlchemy function parameter to the name of the SQLite database file. A Base class was declared using the SQLAlchemy `automap_base()` function. This Base class was necessary because we first needed to create an instance of the database. Then, we could reflect this instance (Base) so that the tables of the database could be iterated through using our python code and SQLAlchemy queries. References were assigned to the variable `Measurement` and `Station`. We would then reference these variables as the tables through out our SQLite queries. The code block was summarized below:

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


## Bulleted List Results

* From all years in the `hawaii.sqlite` database, the mean temperature in Hawaii in the month of June was 74.94. The mean temperature in Hawaii the month of December was 71.04 There is a marginal difference of 3.9 degrees in the average temperature between the months of June and December. 

* Highlighting the pleasant nature of the Hawaiian weather, we can see that the first quartile of the data was at a temperature of 69 degrees. This meant that 75% of the temperature measurements were above 69 degrees. Statistically, a surfer would experience amazing 69 degree or higher temperature 75% of the time even in the month of December! This same logic applies to the temperature in the months of June. Since the first quartile of the data is at 74 degrees, 75% of the temperature readings from June are above 74 degrees. This is also highly farorable for Surfing and Ice cream.

* There were less measurements taken in the month of December compared to June. December had 1517 temperature measurements taken and June had 1700 temperature measurements. If the previous 1517 measurements were accurate for the actual temperature exhibited in December, then additional measurements for December would likely not change the statistics. For example, if 200 more measurements had been taken in the month of December, the mean would likely not change if the measurements were already accurate. However, if the additional measurements taken in December had caused the mean temperature to decrease, then it would suggest that the original temperature measurements in December did not have high accuracy.






## Summary

From the statistical analysis of the summary tables we constructed for June and December, the mean tempeartures in these months were 74.94 and 71.04 respectively. A small difference of 3.9 degrees in the average temperature between the months of June and December illustrated a high likelihood of favorable weather year-long for surfing and ice cream. This suggested that the location and weather would be the perfect conditions for the Surf and Ice Cream Shop and that the company could likely be successful. To further support this claim, the first quartile of temperature measurements for both June and December was at least 69 degrees. This suggested that 75% of the time, the weather would be highly favorable, and at least 69 degrees at this specific location. However, it might be possible that more measurements in the months of June and December could change the statistics such as the average temperature. We would only be able to tell if there was a larger sample of measurements for the next couple of years to compare to these previous measurements. One final precaution for fairweather consumers or inestors at the Surf and Ice Cream shop would be that the minimum temperature in the month of december was 56 degrees. This temperature would not be ideal for surfing or ice cream. To counter this, and further bolster investment support of the business, the high temperatures for the months of June and December were respectively 85 and 83 degrees. Overall, these temperature measurements would be highly conducive to the success of a "Surf and Ice Cream Shop" in Hawaii.

### Additional Queries

If W. Avy wanted even more evidence to reinforce his investment decision he would need to see how the temperature measurement from each station lead to a very high degree of accuracy determining the average temeprature for each month.

The first additional query we performed was to show that the average temperature taken in June was the same for all nine weather stations. To do this, we selected for the `Station.station` name and the average of all the temperature measurements at each station `func.avg(Measurement.obs)`. We again filtered the query by the date for June and used the `group_by()` function to group each average June temperature by the station name. We stored the results of the query in a dataframe. The resulting dataframe below showed that the temperatures taken at each station were identical. This was because the average temperature for each station in the month of June was the same. The high degree of accuracy in temperature measurements for each station was great data to help reinforce W. Avy's decision to invest in the Surf and Ice Cream shop.

`June_stations = session.query(Station.station, func.avg(Measurement.tobs)).\`

&nbsp;&nbsp;&nbsp;&nbsp;`filter(Measurement.date.like('%-06-%')).\`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`group_by(Station.station)`

`june_stations_df = pd.DataFrame(June_stations, columns=["Station_id"," Avg June Temp"])`

`june_stations_df`

![june_stations_df](https://github.com/willmino/surfs_up/blob/main/images/June_stations.png)

We performed one final query to highlight the accuracy of the data and help convince W. Avy that the conditions could not be more perfect for his business investment in the store. This query selected all of the `Station.station` names for for temperature measurements in December from all years. We then stored the data in a dataframe. We can see there are were 13653 different measurements taken in Hawaii. After performing the `.describe()` function, we could see that the same mean December temperature was seen as before at 71.04 degrees.

`December_stations = session.query(Station.station, Measurement.tobs).\`

&nbsp;&nbsp;&nbsp;&nbsp;`filter(Measurement.date.like('%-12-%')).\`

`december_stations_df = pd.DataFrame(December_stations, columns=["Station_id"," Avg December Temps"])`

`december_stations_df.describe()`

![December_stations](https://github.com/willmino/surfs_up/blob/main/images/December_stations.png)

