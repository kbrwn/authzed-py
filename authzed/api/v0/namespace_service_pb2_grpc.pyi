"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import authzed.api.v0.namespace_service_pb2
import grpc

class NamespaceServiceStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    ReadConfig: grpc.UnaryUnaryMultiCallable[
        authzed.api.v0.namespace_service_pb2.ReadConfigRequest,
        authzed.api.v0.namespace_service_pb2.ReadConfigResponse,
    ]
    WriteConfig: grpc.UnaryUnaryMultiCallable[
        authzed.api.v0.namespace_service_pb2.WriteConfigRequest,
        authzed.api.v0.namespace_service_pb2.WriteConfigResponse,
    ]
    DeleteConfigs: grpc.UnaryUnaryMultiCallable[
        authzed.api.v0.namespace_service_pb2.DeleteConfigsRequest,
        authzed.api.v0.namespace_service_pb2.DeleteConfigsResponse,
    ]

class NamespaceServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def ReadConfig(
        self,
        request: authzed.api.v0.namespace_service_pb2.ReadConfigRequest,
        context: grpc.ServicerContext,
    ) -> authzed.api.v0.namespace_service_pb2.ReadConfigResponse: ...
    @abc.abstractmethod
    def WriteConfig(
        self,
        request: authzed.api.v0.namespace_service_pb2.WriteConfigRequest,
        context: grpc.ServicerContext,
    ) -> authzed.api.v0.namespace_service_pb2.WriteConfigResponse: ...
    @abc.abstractmethod
    def DeleteConfigs(
        self,
        request: authzed.api.v0.namespace_service_pb2.DeleteConfigsRequest,
        context: grpc.ServicerContext,
    ) -> authzed.api.v0.namespace_service_pb2.DeleteConfigsResponse: ...

def add_NamespaceServiceServicer_to_server(servicer: NamespaceServiceServicer, server: grpc.Server) -> None: ...
