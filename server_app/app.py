# File to run the server
from concurrent import futures
import grpc

from server_app.generated import time_series_pb2_grpc
from server_app.grpc_classes import TimeSeriesServer


class Server:

    @staticmethod
    def run(port: int = 50051) -> None:
        """
        Run a gRPC server.
        :param port: port in which the server will be exposed.
        :return: None
        """
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        time_series_pb2_grpc.add_TimeSeriesServicer_to_server(TimeSeriesServer(), server)
        server.add_insecure_port('[::]:{}'.format(str(port)))
        server.start()
        print('Server is running!')
        server.wait_for_termination()
