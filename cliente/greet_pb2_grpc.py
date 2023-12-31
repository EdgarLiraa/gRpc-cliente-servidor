# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import greet_pb2 as greet__pb2


class GreeterStub(object):
    """The greeting service definition.

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.VoidTeste = channel.unary_unary(
                '/greet.Greeter/VoidTeste',
                request_serializer=greet__pb2.VoidRequest.SerializeToString,
                response_deserializer=greet__pb2.VoidReply.FromString,
                )
        self.LongSimplesTeste = channel.unary_unary(
                '/greet.Greeter/LongSimplesTeste',
                request_serializer=greet__pb2.LongRequest.SerializeToString,
                response_deserializer=greet__pb2.LongReply.FromString,
                )
        self.LongComplexoTeste = channel.unary_unary(
                '/greet.Greeter/LongComplexoTeste',
                request_serializer=greet__pb2.LongComplexRequest.SerializeToString,
                response_deserializer=greet__pb2.LongComplexReply.FromString,
                )
        self.StringTeste = channel.unary_unary(
                '/greet.Greeter/StringTeste',
                request_serializer=greet__pb2.StringRequest.SerializeToString,
                response_deserializer=greet__pb2.StringReply.FromString,
                )
        self.ClassTeste = channel.unary_unary(
                '/greet.Greeter/ClassTeste',
                request_serializer=greet__pb2.ClasseRequest.SerializeToString,
                response_deserializer=greet__pb2.ClasseReply.FromString,
                )


class GreeterServicer(object):
    """The greeting service definition.

    """

    def VoidTeste(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LongSimplesTeste(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LongComplexoTeste(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StringTeste(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ClassTeste(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GreeterServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'VoidTeste': grpc.unary_unary_rpc_method_handler(
                    servicer.VoidTeste,
                    request_deserializer=greet__pb2.VoidRequest.FromString,
                    response_serializer=greet__pb2.VoidReply.SerializeToString,
            ),
            'LongSimplesTeste': grpc.unary_unary_rpc_method_handler(
                    servicer.LongSimplesTeste,
                    request_deserializer=greet__pb2.LongRequest.FromString,
                    response_serializer=greet__pb2.LongReply.SerializeToString,
            ),
            'LongComplexoTeste': grpc.unary_unary_rpc_method_handler(
                    servicer.LongComplexoTeste,
                    request_deserializer=greet__pb2.LongComplexRequest.FromString,
                    response_serializer=greet__pb2.LongComplexReply.SerializeToString,
            ),
            'StringTeste': grpc.unary_unary_rpc_method_handler(
                    servicer.StringTeste,
                    request_deserializer=greet__pb2.StringRequest.FromString,
                    response_serializer=greet__pb2.StringReply.SerializeToString,
            ),
            'ClassTeste': grpc.unary_unary_rpc_method_handler(
                    servicer.ClassTeste,
                    request_deserializer=greet__pb2.ClasseRequest.FromString,
                    response_serializer=greet__pb2.ClasseReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'greet.Greeter', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Greeter(object):
    """The greeting service definition.

    """

    @staticmethod
    def VoidTeste(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/greet.Greeter/VoidTeste',
            greet__pb2.VoidRequest.SerializeToString,
            greet__pb2.VoidReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LongSimplesTeste(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/greet.Greeter/LongSimplesTeste',
            greet__pb2.LongRequest.SerializeToString,
            greet__pb2.LongReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LongComplexoTeste(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/greet.Greeter/LongComplexoTeste',
            greet__pb2.LongComplexRequest.SerializeToString,
            greet__pb2.LongComplexReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StringTeste(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/greet.Greeter/StringTeste',
            greet__pb2.StringRequest.SerializeToString,
            greet__pb2.StringReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ClassTeste(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/greet.Greeter/ClassTeste',
            greet__pb2.ClasseRequest.SerializeToString,
            greet__pb2.ClasseReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
