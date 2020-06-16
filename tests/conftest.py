import pytest


@pytest.fixture(scope='module')
def grpc_add_to_server():
    from server_app.generated.time_series_pb2_grpc import add_TimeSeriesServicer_to_server

    return add_TimeSeriesServicer_to_server


@pytest.fixture(scope='module')
def grpc_servicer():
    from server_app.grpc_classes import TimeSeriesServer

    return TimeSeriesServer()


@pytest.fixture(scope='module')
def grpc_stub(grpc_channel):
    from server_app.generated.time_series_pb2_grpc import TimeSeriesStub

    return TimeSeriesStub(grpc_channel)
