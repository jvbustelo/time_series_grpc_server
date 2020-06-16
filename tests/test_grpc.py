from server_app.generated import time_series_pb2


def test_reply(grpc_stub):
    request = time_series_pb2.TimeSeriesRequest()
    response = grpc_stub.Reply(request)

    assert hasattr(response, 'data_points')
    assert isinstance(response.data_points[0].time, str)
    assert isinstance(response.data_points[0].meterusage, float)
