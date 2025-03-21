import requests
import pandas as pd


# create WeatherData class to hold variables
class WeatherData:
    def __init__(self, latitude, longitude, month, day, year):
        self.weather_data = None
        self.latitude = latitude
        self.longitude = longitude
        self.month = month
        self.day = day
        self.year = year
        self.ave_temperature = None
        self.min_temperature = None
        self.max_temperature = None
        self.ave_wind_speed = None
        self.min_wind_speed = None
        self.max_wind_speed = None
        self.sum_precipitation = None
        self.min_precipitation = None
        self.max_precipitation = None

    # creating a function to query the API
    def get_weather_data(self):
        url = f'https://archive-api.open-meteo.com/v1/archive?latitude={self.latitude}&longitude={self.longitude}&start_date=2020-05-01&end_date={self.year}-{self.month}-{self.day}&daily=temperature_2m_max,precipitation_sum,wind_speed_10m_max&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch&timezone=GMT'
        response = requests.get(url)
        response = response.json()

        # Create a DataFrame from the data
        df = pd.DataFrame({
            'latitude': [self.latitude] * len(response['daily']['time']),
            'longitude': [self.longitude] * len(response['daily']['time']),
            'month': [self.month] * len(response['daily']['time']),
            'day': [self.day] * len(response['daily']['time']),
            'year': [self.year] * len(response['daily']['time']),
            'date': response['daily']['time'],
            'temp': response['daily']['temperature_2m_max'],
            'precipitation': response['daily']['precipitation_sum'],
            'wind_speed': response['daily']['wind_speed_10m_max']

        })

        # Storing the DataFrame in the class
        self.weather_data = df

    # Creating a function to filter the data from the API for the day 5/1 for each year from 2020-2024

    def filter_data(self):
        self.weather_data['date'] = pd.to_datetime(
            self.weather_data['date'])  # Changes date column to datetime format
        self.weather_data = self.weather_data[
            self.weather_data['date'].dt.month == 5]  # Filtering rows where the month is 5
        # filter rows where the day is 1
        self.weather_data = self.weather_data[self.weather_data['date'].dt.day == 1]

        self.latitude = self.latitude
        self.longitude = self.longitude
        self.month = self.month
        self.day = self.day
        self.year = self.year
        self.ave_temperature = self.calc_ave_temp()

    # Part C2 Created functions to get calculated values.

    def calc_ave_temp(self):
        self.ave_temperature = round(self.weather_data['temp'].mean(), 2)
        return self.ave_temperature

    def calc_min_temp(self):
        self.min_temperature = self.weather_data['temp'].min()
        return self.min_temperature

    def calc_max_temp(self):
        self.max_temperature = self.weather_data['temp'].max()
        return self.max_temperature

    def calc_precipitation_sum(self):
        self.sum_precipitation = self.weather_data['precipitation'].sum()
        return self.sum_precipitation

    def calc_precipitation_min(self):
        self.min_precipitation = self.weather_data['precipitation'].min()
        return self.min_precipitation

    def calc_precipitation_max(self):
        self.max_precipitation = self.weather_data['precipitation'].max()
        return self.max_precipitation

    def calc_max_wind_speed(self):
        self.max_wind_speed = self.weather_data['wind_speed'].max()
        return self.max_wind_speed

    def calc_min_wind_speed(self):
        self.min_wind_speed = self.weather_data['wind_speed'].min()
        return self.min_wind_speed

    def calc_ave_wind_speed(self):
        self.ave_wind_speed = self.weather_data['wind_speed'].mean()
        return self.ave_wind_speed

    # Created a method to print values required for Part C3
    def print_weather_summary(self):
        print()
        print('\033[91m' + 'Weather values from zipcode 50703 on May 1 for years 2020-2024:' + '\033[0m')
        print(f'- Mean temperature in Fahrenheit 5/1 for the last 5 years {self.ave_temperature}.\n')
        print(f'- Max wind speed in MPH from 5/1 for the last 5 years {self.max_wind_speed}.\n')
        print(f'- The sum of daily precipitation for 5/1 for the last 5 years {self.sum_precipitation}.\n')
