from server_app.cons_data_retriever import ConsDataRetriever
from server_app.data_points_creator import DataPointsCreator
from server_app.generated.time_series_pb2 import TimeSeriesReply


class TimeSeriesReplyCreator:

    @staticmethod
    def create_reply() -> TimeSeriesReply:
        """
        Create the gRPC reply object based on the meter readings.
        :return:
        """
        reply = TimeSeriesReply()
        readings = ConsDataRetriever.get_meterusage_readings()
        data_points = DataPointsCreator.data_points_from_readings(readings)
        reply.data_points.extend(data_points)
        return reply
