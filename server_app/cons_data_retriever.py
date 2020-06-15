import os
from typing import List

from server_app.models import MeterReading
# import pandas as pd
import csv


class ConsDataRetriever:
    """
    Class which contains functions to retrieve data from different readings and with different methods.

    Assessment note: For now it only contains one method, but the class is intended to be extended with other data
    retrieving methods and for other sensors.
    """

    @staticmethod
    def get_meterusage_readings(file_path: str = 'data/meterusage.csv') -> List[MeterReading]:
        """
        Retrieve and format the meter readings from the specified csv file.
        :param file_path: path where the file is located relative to the project's root directory.
        :return: time series of the meter readings
        """
        readings = []
        project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(project_path, file_path)
        with open(file_path, 'r') as file:
            my_reader = csv.reader(file, delimiter=',')
            column_headers = next(my_reader)  # Skip the header
            for row in my_reader:
                reading = MeterReading()
                reading.time = row[0]
                reading.meterusage = float(row[1])
                readings.append(reading)

        return readings


class ConsDataRetrieverWithPandas:
    """
    Assessment note: This class is another option to read the CSV data. Initially, I thought about this design since it
    would allow for much more verbose and intuitive data manipulation (e.g. using column names versus using indexes in
    the ConsDataRetriever version). However, it implies looping through the data one time more w.r.t. ConsDataRetriever.
    Finally, I decided to go for the uglier data manipulation version since it is a very easy dataset. If things were
    to get more complex, I would probably go for the pandas option.

    To use this version, pip install pandas, uncomment the import statement at the top of this file and change the
    usage of ConsDataRetriever to ConsDataRetrieverWithPandas.
    """

    @staticmethod
    def get_meterusage_readings(file_path: str = 'data/meterusage.csv') -> List[MeterReading]:
        """
        Retrieve and format the meter readings from the provided csv file.
        :param file_path: path where the file is located relative to the project's root directory.
        :return: list of meter readings
        """
        readings = []
        project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(project_path, file_path)
        df = pd.read_csv(file_path)
        for row in df.iterrows():
            reading = MeterReading()
            reading.time = row[1]['time']
            reading.meterusage = row[1]['meterusage']
            readings.append(reading)

        return readings
