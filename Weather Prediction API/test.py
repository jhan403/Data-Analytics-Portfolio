import pytest
from weather_data import WeatherData
from weather_data_table import WeatherDataTable


# Testing that the weather_data function gets data
def test_get_weather_data():
    weather_data = WeatherData(42.4928, -92.343, '05', '01', 2024)
    weather_data.get_weather_data()
    assert weather_data.weather_data is not None, "Failed to get weather data"


def test_weather_data_init():
    # made an instance of the WeatherData class
    weather_data = WeatherData(42.4928, -92.343, '05', '01', 2024)

    # Tested that the attributes are correctly set
    assert weather_data.latitude == 42.4928
    assert weather_data.longitude == -92.343
    assert weather_data.month == '05'
    assert weather_data.day == '01'
    assert weather_data.year == 2024


# Testing that data is retrieved from the database
def test_retrieve_data():
    df = WeatherDataTable.retrieve_data()
    assert not df.empty, "Failed to retrieve data from the database"
