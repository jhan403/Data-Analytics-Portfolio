# Weather Prediction API Application Version 1.1

This application makes use of the weather API provided by Open-Meteo.com 
to query max temperature, total precipitation, and max wind speed for each day from the last five years. 
Then the data is filtered to provide the above data for May 1st of each year.
Calculations are performed on the data to provide the mean, max and min values for wind speed and temperature.
Every precipitation total for May 1st of each year is added together to find the total precipitation 
for May 1st of the last five years as well as the min and max values for that date range.

The 'weather_data' database is created and all filtered data is inserted into a table named 'weather_data_table'
Finally, the data is queried from the 'weather_data_table' and displayed in a Pandas dataframe.


## Installation

Instructions on how to install the required dependencies for this project and how to run tests.:

```bash
pip install -r requirements.txt

# Instructions on how to run provided tests using a terminal.
pytest test.py