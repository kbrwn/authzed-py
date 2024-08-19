# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: authzed/api/v1/error_reason.proto
# Protobuf Python Version: 5.27.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    3,
    '',
    'authzed/api/v1/error_reason.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!authzed/api/v1/error_reason.proto\x12\x0e\x61uthzed.api.v1*\xf1\t\n\x0b\x45rrorReason\x12\x1c\n\x18\x45RROR_REASON_UNSPECIFIED\x10\x00\x12#\n\x1f\x45RROR_REASON_SCHEMA_PARSE_ERROR\x10\x01\x12\"\n\x1e\x45RROR_REASON_SCHEMA_TYPE_ERROR\x10\x02\x12#\n\x1f\x45RROR_REASON_UNKNOWN_DEFINITION\x10\x03\x12/\n+ERROR_REASON_UNKNOWN_RELATION_OR_PERMISSION\x10\x04\x12,\n(ERROR_REASON_TOO_MANY_UPDATES_IN_REQUEST\x10\x05\x12\x32\n.ERROR_REASON_TOO_MANY_PRECONDITIONS_IN_REQUEST\x10\x06\x12\x35\n1ERROR_REASON_WRITE_OR_DELETE_PRECONDITION_FAILURE\x10\x07\x12\"\n\x1e\x45RROR_REASON_SERVICE_READ_ONLY\x10\x08\x12\x1f\n\x1b\x45RROR_REASON_UNKNOWN_CAVEAT\x10\t\x12%\n!ERROR_REASON_INVALID_SUBJECT_TYPE\x10\n\x12,\n(ERROR_REASON_CAVEAT_PARAMETER_TYPE_ERROR\x10\x0b\x12-\n)ERROR_REASON_UPDATES_ON_SAME_RELATIONSHIP\x10\x0c\x12)\n%ERROR_REASON_CANNOT_UPDATE_PERMISSION\x10\r\x12(\n$ERROR_REASON_CAVEAT_EVALUATION_ERROR\x10\x0e\x12\x1f\n\x1b\x45RROR_REASON_INVALID_CURSOR\x10\x0f\x12@\n<ERROR_REASON_TOO_MANY_RELATIONSHIPS_FOR_TRANSACTIONAL_DELETE\x10\x10\x12.\n*ERROR_REASON_MAX_RELATIONSHIP_CONTEXT_SIZE\x10\x11\x12\x31\n-ERROR_REASON_ATTEMPT_TO_RECREATE_RELATIONSHIP\x10\x12\x12\'\n#ERROR_REASON_MAXIMUM_DEPTH_EXCEEDED\x10\x13\x12&\n\"ERROR_REASON_SERIALIZATION_FAILURE\x10\x14\x12+\n\'ERROR_REASON_TOO_MANY_CHECKS_IN_REQUEST\x10\x15\x12\x30\n,ERROR_REASON_EXCEEDS_MAXIMUM_ALLOWABLE_LIMIT\x10\x16\x12\x1f\n\x1b\x45RROR_REASON_INVALID_FILTER\x10\x17\x12\x35\n1ERROR_REASON_INMEMORY_TOO_MANY_CONCURRENT_UPDATES\x10\x18\x12#\n\x1f\x45RROR_REASON_EMPTY_PRECONDITION\x10\x19\x12+\n\'ERROR_REASON_COUNTER_ALREADY_REGISTERED\x10\x1a\x12\'\n#ERROR_REASON_COUNTER_NOT_REGISTERED\x10\x1b\x12%\n!ERROR_REASON_WILDCARD_NOT_ALLOWED\x10\x1c\x42J\n\x12\x63om.authzed.api.v1P\x01Z2github.com/authzed/authzed-go/proto/authzed/api/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'authzed.api.v1.error_reason_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\022com.authzed.api.v1P\001Z2github.com/authzed/authzed-go/proto/authzed/api/v1'
  _globals['_ERRORREASON']._serialized_start=54
  _globals['_ERRORREASON']._serialized_end=1319
# @@protoc_insertion_point(module_scope)
