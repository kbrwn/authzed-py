"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import authzed.api.v0.watch_service_pb2
import collections.abc
import grpc

class WatchServiceStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    Watch: grpc.UnaryStreamMultiCallable[
        authzed.api.v0.watch_service_pb2.WatchRequest,
        authzed.api.v0.watch_service_pb2.WatchResponse,
    ]

class WatchServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def Watch(
        self,
        request: authzed.api.v0.watch_service_pb2.WatchRequest,
        context: grpc.ServicerContext,
    ) -> collections.abc.Iterator[authzed.api.v0.watch_service_pb2.WatchResponse]: ...

def add_WatchServiceServicer_to_server(servicer: WatchServiceServicer, server: grpc.Server) -> None: ...
