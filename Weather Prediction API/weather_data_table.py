from sqlalchemy import create_engine, Column, Integer, Float
from sqlalchemy.orm import sessionmaker, declarative_base
import pandas as pd

# Start the database engine
Base = declarative_base()
engine = create_engine('sqlite:///weather_data.db')
Session = sessionmaker(bind=engine)


# Create class to create table for data
class WeatherDataTable(Base):
    __tablename__ = 'weather_data_table'

    id = Column(Integer, primary_key=True)
    latitude = Column(Float)
    longitude = Column(Float)
    month = Column(Integer)
    day = Column(Integer)
    year = Column(Integer)
    ave_temperature = Column(Float)
    min_temperature = Column(Float)
    max_temperature = Column(Float)
    ave_wind_speed = Column(Float)
    min_wind_speed = Column(Float)
    max_wind_speed = Column(Float)
    sum_precipitation = Column(Float)
    min_precipitation = Column(Float)
    max_precipitation = Column(Float)

    @staticmethod
    def add_weather_data(weather_data):
        # Create a session to interact with the database
        session = Session()

        session.query(WeatherDataTable).delete()

        # Enter data into table with data from WeatherData
        new_entry = WeatherDataTable(
            latitude=weather_data.latitude,
            longitude=weather_data.longitude,
            month=weather_data.month,
            day=weather_data.day,
            year=weather_data.year,
            ave_temperature=weather_data.ave_temperature,
            min_temperature=weather_data.min_temperature,
            max_temperature=weather_data.max_temperature,
            ave_wind_speed=weather_data.ave_wind_speed,
            min_wind_speed=weather_data.min_wind_speed,
            max_wind_speed=weather_data.max_wind_speed,
            sum_precipitation=weather_data.sum_precipitation,
            min_precipitation=weather_data.min_precipitation,
            max_precipitation=weather_data.max_precipitation
        )

        # Add the new entry
        session.add(new_entry)

        # Commit and save changes to the database
        session.commit()

        # Close the session
        session.close()

    @staticmethod
    def retrieve_data():
        session = Session()

        # Query the table
        data2 = session.query(WeatherDataTable).all()

        session.close()
        # create a pandas dataframe of the table values
        df = pd.DataFrame([{
            'latitude': row.latitude,
            'longitude': row.longitude,
            'month': row.month,
            'day': row.day,
            'year': row.year,
            'ave_temperature': row.ave_temperature,
            'min_temperature': row.min_temperature,
            'max_temperature': row.max_temperature,
            'ave_wind_speed': row.ave_wind_speed,
            'min_wind_speed': row.min_wind_speed,
            'max_wind_speed': row.max_wind_speed,
            'sum_precipitation': row.sum_precipitation,
            'min_precipitation': row.min_precipitation,
            'max_precipitation': row.max_precipitation
        } for row in data2])

        # Return the DataFrame
        return df
