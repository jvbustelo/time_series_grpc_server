from typing import List

from server_app.generated.time_series_pb2 import TimeSeriesReply
from server_app.models import MeterReading


class DataPointsCreator:

    @staticmethod
    def data_points_from_readings(readings: List[MeterReading]) -> List[TimeSeriesReply.DataPoint]:
        """
        Generate the list of gRPC DataPoint objects based on a time series of meter readings.
        :param readings: time series of meter readings
        :return:
        """
        data_points = []
        for point in readings:
            data_points.append(TimeSeriesReply.DataPoint(time=point.time, meterusage=point.meterusage))
        return data_points
