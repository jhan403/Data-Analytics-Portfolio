from weather_data import WeatherData
from weather_data_table import WeatherDataTable, Base, engine
import pandas as pd

# Creating a sqlite database and the table
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Creating an instance of the WeatherData class
weather_data = WeatherData(42.4928, -92.343, '05', '01', 2024)

# Calling the get_weather_data method to pull data from API
weather_data.get_weather_data()

# Calling weather_data_filter method to filter API data to include only info for May 1st of year from 2020-2024
weather_data.filter_data()

# Calling methods to get daily weather variables for location and date
weather_data.calc_ave_temp()
weather_data.calc_max_wind_speed()
weather_data.calc_precipitation_sum()
# Calling methods for additional variables to insert data into database
weather_data.calc_min_temp()
weather_data.calc_max_temp()
weather_data.calc_precipitation_min()
weather_data.calc_precipitation_max()
weather_data.calc_min_wind_speed()
weather_data.calc_ave_wind_speed()

# Calling method to print required data from C2
weather_data.print_weather_summary()


# Add the weather data to the database
WeatherDataTable.add_weather_data(weather_data)

# Querying the data from the database
df = WeatherDataTable.retrieve_data()

# Set the option to display all columns
pd.set_option('display.max_columns', None)

# Print the DataFrame

print(df)
