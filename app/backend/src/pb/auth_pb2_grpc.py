# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from pb import auth_pb2 as pb_dot_auth__pb2


class AuthStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Login = channel.unary_unary(
                '/auth.Auth/Login',
                request_serializer=pb_dot_auth__pb2.LoginRequest.SerializeToString,
                response_deserializer=pb_dot_auth__pb2.LoginResponse.FromString,
                )
        self.Signup = channel.unary_unary(
                '/auth.Auth/Signup',
                request_serializer=pb_dot_auth__pb2.SignupRequest.SerializeToString,
                response_deserializer=pb_dot_auth__pb2.SignupResponse.FromString,
                )
        self.Authenticate = channel.unary_unary(
                '/auth.Auth/Authenticate',
                request_serializer=pb_dot_auth__pb2.AuthRequest.SerializeToString,
                response_deserializer=pb_dot_auth__pb2.AuthResponse.FromString,
                )
        self.Deauthenticate = channel.unary_unary(
                '/auth.Auth/Deauthenticate',
                request_serializer=pb_dot_auth__pb2.DeauthRequest.SerializeToString,
                response_deserializer=pb_dot_auth__pb2.DeauthResponse.FromString,
                )


class AuthServicer(object):
    """Missing associated documentation comment in .proto file"""

    def Login(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Signup(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Authenticate(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Deauthenticate(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AuthServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Login': grpc.unary_unary_rpc_method_handler(
                    servicer.Login,
                    request_deserializer=pb_dot_auth__pb2.LoginRequest.FromString,
                    response_serializer=pb_dot_auth__pb2.LoginResponse.SerializeToString,
            ),
            'Signup': grpc.unary_unary_rpc_method_handler(
                    servicer.Signup,
                    request_deserializer=pb_dot_auth__pb2.SignupRequest.FromString,
                    response_serializer=pb_dot_auth__pb2.SignupResponse.SerializeToString,
            ),
            'Authenticate': grpc.unary_unary_rpc_method_handler(
                    servicer.Authenticate,
                    request_deserializer=pb_dot_auth__pb2.AuthRequest.FromString,
                    response_serializer=pb_dot_auth__pb2.AuthResponse.SerializeToString,
            ),
            'Deauthenticate': grpc.unary_unary_rpc_method_handler(
                    servicer.Deauthenticate,
                    request_deserializer=pb_dot_auth__pb2.DeauthRequest.FromString,
                    response_serializer=pb_dot_auth__pb2.DeauthResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'auth.Auth', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Auth(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def Login(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/auth.Auth/Login',
            pb_dot_auth__pb2.LoginRequest.SerializeToString,
            pb_dot_auth__pb2.LoginResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Signup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/auth.Auth/Signup',
            pb_dot_auth__pb2.SignupRequest.SerializeToString,
            pb_dot_auth__pb2.SignupResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Authenticate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/auth.Auth/Authenticate',
            pb_dot_auth__pb2.AuthRequest.SerializeToString,
            pb_dot_auth__pb2.AuthResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Deauthenticate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/auth.Auth/Deauthenticate',
            pb_dot_auth__pb2.DeauthRequest.SerializeToString,
            pb_dot_auth__pb2.DeauthResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)