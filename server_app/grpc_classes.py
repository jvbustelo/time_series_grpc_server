# Keeps all the gRPC specific code
from grpc._server import _Context

from server_app.generated import time_series_pb2_grpc, time_series_pb2
from server_app.reply_creators import TimeSeriesReplyCreator


class TimeSeriesServer(time_series_pb2_grpc.TimeSeriesServicer):

    def Reply(self, request: time_series_pb2.TimeSeriesRequest, context: _Context) -> time_series_pb2.TimeSeriesReply:
        """
        Generate the gRPC reply object to be sent to the client.
        :param request:
        :param context:
        :return:
        """
        reply = TimeSeriesReplyCreator.create_reply()
        return reply
