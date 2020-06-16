from server_app.data_points_creator import DataPointsCreator
from server_app.generated.time_series_pb2 import TimeSeriesReply
from server_app.models import MeterReading


def test_data_points_creator():
    meter_reading = MeterReading()
    meter_reading.time = '0000-00-00 00:00:00'
    meter_reading.meterusage = 1.0
    test_readings = [
        meter_reading
    ]
    test_data_points = DataPointsCreator.data_points_from_readings(test_readings)
    print(test_data_points[0].meterusage)

    assert isinstance(test_data_points, list)
    assert len(test_data_points) == 1
    assert isinstance(test_data_points[0], TimeSeriesReply.DataPoint)
    assert test_data_points[0].time == '0000-00-00 00:00:00'
    assert test_data_points[0].meterusage == 1.0
