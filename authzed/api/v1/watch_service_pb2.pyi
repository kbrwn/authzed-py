"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import authzed.api.v1.core_pb2
import authzed.api.v1.permission_service_pb2
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.struct_pb2
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class WatchRequest(google.protobuf.message.Message):
    """WatchRequest specifies the object definitions for which we want to start
    watching mutations, and an optional start snapshot for when to start
    watching.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OPTIONAL_OBJECT_TYPES_FIELD_NUMBER: builtins.int
    OPTIONAL_START_CURSOR_FIELD_NUMBER: builtins.int
    OPTIONAL_RELATIONSHIP_FILTERS_FIELD_NUMBER: builtins.int
    @property
    def optional_object_types(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """optional_object_types is a filter of resource object types to watch for changes.
        If specified, only changes to the specified object types will be returned and
        optional_relationship_filters cannot be used.
        """

    @property
    def optional_start_cursor(self) -> authzed.api.v1.core_pb2.ZedToken:
        """optional_start_cursor is the ZedToken holding the point-in-time at
        which to start watching for changes.
        If not specified, the watch will begin at the current head revision
        of the datastore, returning any updates that occur after the caller
        makes the request.
        Note that if this cursor references a point-in-time containing data
        that has been garbage collected, an error will be returned.
        """

    @property
    def optional_relationship_filters(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[authzed.api.v1.permission_service_pb2.RelationshipFilter]:
        """optional_relationship_filters, if specified, indicates the
        filter(s) to apply to each relationship to be returned by watch.
        The relationship will be returned as long as at least one filter matches,
        this allows clients to match relationships on multiple filters on a single watch call.
        If specified, optional_object_types cannot be used.
        """

    def __init__(
        self,
        *,
        optional_object_types: collections.abc.Iterable[builtins.str] | None = ...,
        optional_start_cursor: authzed.api.v1.core_pb2.ZedToken | None = ...,
        optional_relationship_filters: collections.abc.Iterable[authzed.api.v1.permission_service_pb2.RelationshipFilter] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["optional_start_cursor", b"optional_start_cursor"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["optional_object_types", b"optional_object_types", "optional_relationship_filters", b"optional_relationship_filters", "optional_start_cursor", b"optional_start_cursor"]) -> None: ...

global___WatchRequest = WatchRequest

@typing.final
class WatchResponse(google.protobuf.message.Message):
    """WatchResponse contains all tuple modification events in ascending
    timestamp order, from the requested start snapshot to a snapshot
    encoded in the watch response. The client can use the snapshot to resume
    watching where the previous watch response left off.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    UPDATES_FIELD_NUMBER: builtins.int
    CHANGES_THROUGH_FIELD_NUMBER: builtins.int
    OPTIONAL_TRANSACTION_METADATA_FIELD_NUMBER: builtins.int
    @property
    def updates(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[authzed.api.v1.core_pb2.RelationshipUpdate]:
        """updates are the RelationshipUpdate events that have occurred since the
        last watch response.
        """

    @property
    def changes_through(self) -> authzed.api.v1.core_pb2.ZedToken:
        """changes_through is the ZedToken that represents the point in time
        that the watch response is current through. This token can be used
        in a subsequent WatchRequest to resume watching from this point.
        """

    @property
    def optional_transaction_metadata(self) -> google.protobuf.struct_pb2.Struct:
        """optional_transaction_metadata is an optional field that returns the transaction metadata
        given to SpiceDB during the transaction that produced the changes in this response.
        This field may not exist if no transaction metadata was provided.
        """

    def __init__(
        self,
        *,
        updates: collections.abc.Iterable[authzed.api.v1.core_pb2.RelationshipUpdate] | None = ...,
        changes_through: authzed.api.v1.core_pb2.ZedToken | None = ...,
        optional_transaction_metadata: google.protobuf.struct_pb2.Struct | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["changes_through", b"changes_through", "optional_transaction_metadata", b"optional_transaction_metadata"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["changes_through", b"changes_through", "optional_transaction_metadata", b"optional_transaction_metadata", "updates", b"updates"]) -> None: ...

global___WatchResponse = WatchResponse
