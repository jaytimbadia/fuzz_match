import grpc

import ingestor_pb2
import ingestor_pb2_grpc
from data import source, target

channel = grpc.insecure_channel('localhost:50051')

stub = ingestor_pb2_grpc.fetchStub(channel)

myrequest = ingestor_pb2.request()
myrequest.source.extend(source)
myrequest.target.extend(target)
myrequest.SerializeToString()

response = stub.calculate(myrequest)

print((response))