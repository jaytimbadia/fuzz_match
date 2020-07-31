import grpc
from concurrent import futures
import time

import ingestor_pb2
import ingestor_pb2_grpc

from test import calculate

class CalculateService(ingestor_pb2_grpc.fetchServicer):

    def calculate(self, request, context):
        response = calculate(request)
        return response


server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))

ingestor_pb2_grpc.add_fetchServicer_to_server(
        CalculateService(), server)


# listen on port 50051
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)