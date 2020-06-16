from server_app.cons_data_retriever import ConsDataRetriever
from server_app.models import MeterReading


def test_csv_reading(test_csv_file='data/test_data.csv'):
    test_readings = ConsDataRetriever.get_meterusage_readings(test_csv_file)

    assert isinstance(test_readings, list)
    assert len(test_readings) == 1
    assert isinstance(test_readings[0], MeterReading)
    assert test_readings[0].time == '2020-01-01 00:00:00'
    assert test_readings[0].meterusage == 1.1
