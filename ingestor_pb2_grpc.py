# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import ingestor_pb2 as ingestor__pb2


class fetchStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.calculate = channel.unary_unary(
                '/fetch/calculate',
                request_serializer=ingestor__pb2.request.SerializeToString,
                response_deserializer=ingestor__pb2.response.FromString,
                )


class fetchServicer(object):
    """Missing associated documentation comment in .proto file."""

    def calculate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_fetchServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'calculate': grpc.unary_unary_rpc_method_handler(
                    servicer.calculate,
                    request_deserializer=ingestor__pb2.request.FromString,
                    response_serializer=ingestor__pb2.response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'fetch', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class fetch(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def calculate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fetch/calculate',
            ingestor__pb2.request.SerializeToString,
            ingestor__pb2.response.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
