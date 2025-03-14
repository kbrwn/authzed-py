"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import authzed.api.v1.core_pb2
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.struct_pb2
import google.protobuf.timestamp_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class DebugInformation(google.protobuf.message.Message):
    """DebugInformation defines debug information returned by an API call in a footer when
    requested with a specific debugging header.

    The specific debug information returned will depend on the type of the API call made.

    See the github.com/authzed/authzed-go project for the specific header and footer names.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CHECK_FIELD_NUMBER: builtins.int
    SCHEMA_USED_FIELD_NUMBER: builtins.int
    schema_used: builtins.str
    """schema_used holds the schema used for the request."""
    @property
    def check(self) -> global___CheckDebugTrace:
        """check holds debug information about a check request."""

    def __init__(
        self,
        *,
        check: global___CheckDebugTrace | None = ...,
        schema_used: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["check", b"check"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["check", b"check", "schema_used", b"schema_used"]) -> None: ...

global___DebugInformation = DebugInformation

@typing.final
class CheckDebugTrace(google.protobuf.message.Message):
    """CheckDebugTrace is a recursive trace of the requests made for resolving a CheckPermission
    API call.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _PermissionType:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _PermissionTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[CheckDebugTrace._PermissionType.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        PERMISSION_TYPE_UNSPECIFIED: CheckDebugTrace._PermissionType.ValueType  # 0
        PERMISSION_TYPE_RELATION: CheckDebugTrace._PermissionType.ValueType  # 1
        PERMISSION_TYPE_PERMISSION: CheckDebugTrace._PermissionType.ValueType  # 2

    class PermissionType(_PermissionType, metaclass=_PermissionTypeEnumTypeWrapper): ...
    PERMISSION_TYPE_UNSPECIFIED: CheckDebugTrace.PermissionType.ValueType  # 0
    PERMISSION_TYPE_RELATION: CheckDebugTrace.PermissionType.ValueType  # 1
    PERMISSION_TYPE_PERMISSION: CheckDebugTrace.PermissionType.ValueType  # 2

    class _Permissionship:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _PermissionshipEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[CheckDebugTrace._Permissionship.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        PERMISSIONSHIP_UNSPECIFIED: CheckDebugTrace._Permissionship.ValueType  # 0
        PERMISSIONSHIP_NO_PERMISSION: CheckDebugTrace._Permissionship.ValueType  # 1
        PERMISSIONSHIP_HAS_PERMISSION: CheckDebugTrace._Permissionship.ValueType  # 2
        PERMISSIONSHIP_CONDITIONAL_PERMISSION: CheckDebugTrace._Permissionship.ValueType  # 3

    class Permissionship(_Permissionship, metaclass=_PermissionshipEnumTypeWrapper): ...
    PERMISSIONSHIP_UNSPECIFIED: CheckDebugTrace.Permissionship.ValueType  # 0
    PERMISSIONSHIP_NO_PERMISSION: CheckDebugTrace.Permissionship.ValueType  # 1
    PERMISSIONSHIP_HAS_PERMISSION: CheckDebugTrace.Permissionship.ValueType  # 2
    PERMISSIONSHIP_CONDITIONAL_PERMISSION: CheckDebugTrace.Permissionship.ValueType  # 3

    @typing.final
    class SubProblems(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TRACES_FIELD_NUMBER: builtins.int
        @property
        def traces(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___CheckDebugTrace]: ...
        def __init__(
            self,
            *,
            traces: collections.abc.Iterable[global___CheckDebugTrace] | None = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["traces", b"traces"]) -> None: ...

    RESOURCE_FIELD_NUMBER: builtins.int
    PERMISSION_FIELD_NUMBER: builtins.int
    PERMISSION_TYPE_FIELD_NUMBER: builtins.int
    SUBJECT_FIELD_NUMBER: builtins.int
    RESULT_FIELD_NUMBER: builtins.int
    CAVEAT_EVALUATION_INFO_FIELD_NUMBER: builtins.int
    DURATION_FIELD_NUMBER: builtins.int
    WAS_CACHED_RESULT_FIELD_NUMBER: builtins.int
    SUB_PROBLEMS_FIELD_NUMBER: builtins.int
    OPTIONAL_EXPIRES_AT_FIELD_NUMBER: builtins.int
    TRACE_OPERATION_ID_FIELD_NUMBER: builtins.int
    SOURCE_FIELD_NUMBER: builtins.int
    permission: builtins.str
    """permission holds the name of the permission or relation on which the Check was performed."""
    permission_type: global___CheckDebugTrace.PermissionType.ValueType
    """permission_type holds information indicating whether it was a permission or relation."""
    result: global___CheckDebugTrace.Permissionship.ValueType
    """result holds the result of the Check call."""
    was_cached_result: builtins.bool
    """was_cached_result, if true, indicates that the result was found in the cache and returned directly."""
    trace_operation_id: builtins.str
    """trace_operation_id is a unique identifier for this trace's operation, that will
    be shared for all traces created for the same check operation in SpiceDB.

    In cases where SpiceDB performs automatic batching of subproblems, this ID can be used
    to correlate work that was shared across multiple traces.

    This identifier is generated by SpiceDB, is to be considered opaque to the caller
    and only guaranteed to be unique within the same overall Check or CheckBulk operation.
    """
    source: builtins.str
    """source holds the source of the result. It is of the form:
    `<sourcetype>:<sourceid>`, where sourcetype can be, among others:
    `spicedb`, `materialize`, etc.
    """
    @property
    def resource(self) -> authzed.api.v1.core_pb2.ObjectReference:
        """resource holds the resource on which the Check was performed.
        for batched calls, the object_id field contains a comma-separated list of object IDs
        for all the resources checked in the batch.
        """

    @property
    def subject(self) -> authzed.api.v1.core_pb2.SubjectReference:
        """subject holds the subject on which the Check was performed. This will be static across all calls within
        the same Check tree.
        """

    @property
    def caveat_evaluation_info(self) -> global___CaveatEvalInfo:
        """caveat_evaluation_info holds information about the caveat evaluated for this step of the trace."""

    @property
    def duration(self) -> google.protobuf.duration_pb2.Duration:
        """duration holds the time spent executing this Check operation."""

    @property
    def sub_problems(self) -> global___CheckDebugTrace.SubProblems:
        """sub_problems holds the sub problems that were executed to resolve the answer to this Check. An empty list
        and a permissionship of PERMISSIONSHIP_HAS_PERMISSION indicates the subject was found within this relation.
        """

    @property
    def optional_expires_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """optional_expires_at is the time at which at least one of the relationships used to
        compute this result, expires (if any). This is *not* related to the caching window.
        """

    def __init__(
        self,
        *,
        resource: authzed.api.v1.core_pb2.ObjectReference | None = ...,
        permission: builtins.str = ...,
        permission_type: global___CheckDebugTrace.PermissionType.ValueType = ...,
        subject: authzed.api.v1.core_pb2.SubjectReference | None = ...,
        result: global___CheckDebugTrace.Permissionship.ValueType = ...,
        caveat_evaluation_info: global___CaveatEvalInfo | None = ...,
        duration: google.protobuf.duration_pb2.Duration | None = ...,
        was_cached_result: builtins.bool = ...,
        sub_problems: global___CheckDebugTrace.SubProblems | None = ...,
        optional_expires_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        trace_operation_id: builtins.str = ...,
        source: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["caveat_evaluation_info", b"caveat_evaluation_info", "duration", b"duration", "optional_expires_at", b"optional_expires_at", "resolution", b"resolution", "resource", b"resource", "sub_problems", b"sub_problems", "subject", b"subject", "was_cached_result", b"was_cached_result"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["caveat_evaluation_info", b"caveat_evaluation_info", "duration", b"duration", "optional_expires_at", b"optional_expires_at", "permission", b"permission", "permission_type", b"permission_type", "resolution", b"resolution", "resource", b"resource", "result", b"result", "source", b"source", "sub_problems", b"sub_problems", "subject", b"subject", "trace_operation_id", b"trace_operation_id", "was_cached_result", b"was_cached_result"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["resolution", b"resolution"]) -> typing.Literal["was_cached_result", "sub_problems"] | None: ...

global___CheckDebugTrace = CheckDebugTrace

@typing.final
class CaveatEvalInfo(google.protobuf.message.Message):
    """CaveatEvalInfo holds information about a caveat expression that was evaluated."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Result:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _ResultEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[CaveatEvalInfo._Result.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        RESULT_UNSPECIFIED: CaveatEvalInfo._Result.ValueType  # 0
        RESULT_UNEVALUATED: CaveatEvalInfo._Result.ValueType  # 1
        RESULT_FALSE: CaveatEvalInfo._Result.ValueType  # 2
        RESULT_TRUE: CaveatEvalInfo._Result.ValueType  # 3
        RESULT_MISSING_SOME_CONTEXT: CaveatEvalInfo._Result.ValueType  # 4

    class Result(_Result, metaclass=_ResultEnumTypeWrapper): ...
    RESULT_UNSPECIFIED: CaveatEvalInfo.Result.ValueType  # 0
    RESULT_UNEVALUATED: CaveatEvalInfo.Result.ValueType  # 1
    RESULT_FALSE: CaveatEvalInfo.Result.ValueType  # 2
    RESULT_TRUE: CaveatEvalInfo.Result.ValueType  # 3
    RESULT_MISSING_SOME_CONTEXT: CaveatEvalInfo.Result.ValueType  # 4

    EXPRESSION_FIELD_NUMBER: builtins.int
    RESULT_FIELD_NUMBER: builtins.int
    CONTEXT_FIELD_NUMBER: builtins.int
    PARTIAL_CAVEAT_INFO_FIELD_NUMBER: builtins.int
    CAVEAT_NAME_FIELD_NUMBER: builtins.int
    expression: builtins.str
    """expression is the expression that was evaluated."""
    result: global___CaveatEvalInfo.Result.ValueType
    """result is the result of the evaluation."""
    caveat_name: builtins.str
    """caveat_name is the name of the caveat that was executed, if applicable."""
    @property
    def context(self) -> google.protobuf.struct_pb2.Struct:
        """context consists of any named values that were used for evaluating the caveat expression."""

    @property
    def partial_caveat_info(self) -> authzed.api.v1.core_pb2.PartialCaveatInfo:
        """partial_caveat_info holds information of a partially-evaluated caveated response, if applicable."""

    def __init__(
        self,
        *,
        expression: builtins.str = ...,
        result: global___CaveatEvalInfo.Result.ValueType = ...,
        context: google.protobuf.struct_pb2.Struct | None = ...,
        partial_caveat_info: authzed.api.v1.core_pb2.PartialCaveatInfo | None = ...,
        caveat_name: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["context", b"context", "partial_caveat_info", b"partial_caveat_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["caveat_name", b"caveat_name", "context", b"context", "expression", b"expression", "partial_caveat_info", b"partial_caveat_info", "result", b"result"]) -> None: ...

global___CaveatEvalInfo = CaveatEvalInfo
