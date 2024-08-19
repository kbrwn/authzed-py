# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: authzed/api/v1/permission_service.proto
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
    'authzed/api/v1/permission_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
from validate import validate_pb2 as validate_dot_validate__pb2
from authzed.api.v1 import core_pb2 as authzed_dot_api_dot_v1_dot_core__pb2
from authzed.api.v1 import debug_pb2 as authzed_dot_api_dot_v1_dot_debug__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'authzed/api/v1/permission_service.proto\x12\x0e\x61uthzed.api.v1\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/rpc/status.proto\x1a\x17validate/validate.proto\x1a\x19\x61uthzed/api/v1/core.proto\x1a\x1a\x61uthzed/api/v1/debug.proto\"\x9c\x02\n\x0b\x43onsistency\x12\x34\n\x10minimize_latency\x18\x01 \x01(\x08\x42\x07\xfa\x42\x04j\x02\x08\x01H\x00R\x0fminimizeLatency\x12\x45\n\x11\x61t_least_as_fresh\x18\x02 \x01(\x0b\x32\x18.authzed.api.v1.ZedTokenH\x00R\x0e\x61tLeastAsFresh\x12\x46\n\x11\x61t_exact_snapshot\x18\x03 \x01(\x0b\x32\x18.authzed.api.v1.ZedTokenH\x00R\x0f\x61tExactSnapshot\x12\x34\n\x10\x66ully_consistent\x18\x04 \x01(\x08\x42\x07\xfa\x42\x04j\x02\x08\x01H\x00R\x0f\x66ullyConsistentB\x12\n\x0brequirement\x12\x03\xf8\x42\x01\"\xf5\x03\n\x12RelationshipFilter\x12p\n\rresource_type\x18\x01 \x01(\tBK\xfa\x42HrF(\x80\x01\x32\x41^(([a-z][a-z0-9_]{1,61}[a-z0-9]/)*[a-z][a-z0-9_]{1,62}[a-z0-9])?$R\x0cresourceType\x12W\n\x14optional_resource_id\x18\x02 \x01(\tB%\xfa\x42\"r (\x80\x08\x32\x1b^([a-zA-Z0-9/_|\\-=+]{1,})?$R\x12optionalResourceId\x12\x64\n\x1boptional_resource_id_prefix\x18\x05 \x01(\tB%\xfa\x42\"r (\x80\x08\x32\x1b^([a-zA-Z0-9/_|\\-=+]{1,})?$R\x18optionalResourceIdPrefix\x12W\n\x11optional_relation\x18\x03 \x01(\tB*\xfa\x42\'r%(@2!^([a-z][a-z0-9_]{1,62}[a-z0-9])?$R\x10optionalRelation\x12U\n\x17optional_subject_filter\x18\x04 \x01(\x0b\x32\x1d.authzed.api.v1.SubjectFilterR\x15optionalSubjectFilter\"\x8d\x03\n\rSubjectFilter\x12k\n\x0csubject_type\x18\x01 \x01(\tBH\xfa\x42\x45rC(\x80\x01\x32>^([a-z][a-z0-9_]{1,61}[a-z0-9]/)*[a-z][a-z0-9_]{1,62}[a-z0-9]$R\x0bsubjectType\x12Z\n\x13optional_subject_id\x18\x02 \x01(\tB*\xfa\x42\'r%(\x80\x08\x32 ^(([a-zA-Z0-9/_|\\-=+]{1,})|\\*)?$R\x11optionalSubjectId\x12Y\n\x11optional_relation\x18\x03 \x01(\x0b\x32,.authzed.api.v1.SubjectFilter.RelationFilterR\x10optionalRelation\x1aX\n\x0eRelationFilter\x12\x46\n\x08relation\x18\x01 \x01(\tB*\xfa\x42\'r%(@2!^([a-z][a-z0-9_]{1,62}[a-z0-9])?$R\x08relation\"\xa9\x02\n\x18ReadRelationshipsRequest\x12=\n\x0b\x63onsistency\x18\x01 \x01(\x0b\x32\x1b.authzed.api.v1.ConsistencyR\x0b\x63onsistency\x12]\n\x13relationship_filter\x18\x02 \x01(\x0b\x32\".authzed.api.v1.RelationshipFilterB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01R\x12relationshipFilter\x12.\n\x0eoptional_limit\x18\x03 \x01(\rB\x07\xfa\x42\x04*\x02(\x00R\roptionalLimit\x12?\n\x0foptional_cursor\x18\x04 \x01(\x0b\x32\x16.authzed.api.v1.CursorR\x0eoptionalCursor\"\xec\x01\n\x19ReadRelationshipsResponse\x12;\n\x07read_at\x18\x01 \x01(\x0b\x32\x18.authzed.api.v1.ZedTokenB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01R\x06readAt\x12J\n\x0crelationship\x18\x02 \x01(\x0b\x32\x1c.authzed.api.v1.RelationshipB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01R\x0crelationship\x12\x46\n\x13\x61\x66ter_result_cursor\x18\x03 \x01(\x0b\x32\x16.authzed.api.v1.CursorR\x11\x61\x66terResultCursor\"\x86\x02\n\x0cPrecondition\x12P\n\toperation\x18\x01 \x01(\x0e\x32&.authzed.api.v1.Precondition.OperationB\n\xfa\x42\x07\x82\x01\x04\x10\x01 \x00R\toperation\x12\x44\n\x06\x66ilter\x18\x02 \x01(\x0b\x32\".authzed.api.v1.RelationshipFilterB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01R\x06\x66ilter\"^\n\tOperation\x12\x19\n\x15OPERATION_UNSPECIFIED\x10\x00\x12\x1c\n\x18OPERATION_MUST_NOT_MATCH\x10\x01\x12\x18\n\x14OPERATION_MUST_MATCH\x10\x02\"\xcc\x01\n\x19WriteRelationshipsRequest\x12K\n\x07updates\x18\x01 \x03(\x0b\x32\".authzed.api.v1.RelationshipUpdateB\r\xfa\x42\n\x92\x01\x07\"\x05\x8a\x01\x02\x10\x01R\x07updates\x12\x62\n\x16optional_preconditions\x18\x02 \x03(\x0b\x32\x1c.authzed.api.v1.PreconditionB\r\xfa\x42\n\x92\x01\x07\"\x05\x8a\x01\x02\x10\x01R\x15optionalPreconditions\"U\n\x1aWriteRelationshipsResponse\x12\x37\n\nwritten_at\x18\x01 \x01(\x0b\x32\x18.authzed.api.v1.ZedTokenR\twrittenAt\"\xd8\x02\n\x1a\x44\x65leteRelationshipsRequest\x12]\n\x13relationship_filter\x18\x01 \x01(\x0b\x32\".authzed.api.v1.RelationshipFilterB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01R\x12relationshipFilter\x12\x62\n\x16optional_preconditions\x18\x02 \x03(\x0b\x32\x1c.authzed.api.v1.PreconditionB\r\xfa\x42\n\x92\x01\x07\"\x05\x8a\x01\x02\x10\x01R\x15optionalPreconditions\x12.\n\x0eoptional_limit\x18\x03 \x01(\rB\x07\xfa\x42\x04*\x02(\x00R\roptionalLimit\x12G\n optional_allow_partial_deletions\x18\x04 \x01(\x08R\x1doptionalAllowPartialDeletions\"\xb7\x02\n\x1b\x44\x65leteRelationshipsResponse\x12\x37\n\ndeleted_at\x18\x01 \x01(\x0b\x32\x18.authzed.api.v1.ZedTokenR\tdeletedAt\x12i\n\x11\x64\x65letion_progress\x18\x02 \x01(\x0e\x32<.authzed.api.v1.DeleteRelationshipsResponse.DeletionProgressR\x10\x64\x65letionProgress\"t\n\x10\x44\x65letionProgress\x12!\n\x1d\x44\x45LETION_PROGRESS_UNSPECIFIED\x10\x00\x12\x1e\n\x1a\x44\x45LETION_PROGRESS_COMPLETE\x10\x01\x12\x1d\n\x19\x44\x45LETION_PROGRESS_PARTIAL\x10\x02\"\x90\x03\n\x16\x43heckPermissionRequest\x12=\n\x0b\x63onsistency\x18\x01 \x01(\x0b\x32\x1b.authzed.api.v1.ConsistencyR\x0b\x63onsistency\x12\x45\n\x08resource\x18\x02 \x01(\x0b\x32\x1f.authzed.api.v1.ObjectReferenceB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01R\x08resource\x12J\n\npermission\x18\x03 \x01(\tB*\xfa\x42\'r%(@2!^([a-z][a-z0-9_]{1,62}[a-z0-9])?$R\npermission\x12\x44\n\x07subject\x18\x04 \x01(\x0b\x32 .authzed.api.v1.SubjectReferenceB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01R\x07subject\x12;\n\x07\x63ontext\x18\x05 \x01(\x0b\x32\x17.google.protobuf.StructB\x08\xfa\x42\x05\x8a\x01\x02\x10\x00R\x07\x63ontext\x12!\n\x0cwith_tracing\x18\x06 \x01(\x08R\x0bwithTracing\"\x8b\x04\n\x17\x43heckPermissionResponse\x12\x41\n\nchecked_at\x18\x01 \x01(\x0b\x32\x18.authzed.api.v1.ZedTokenB\x08\xfa\x42\x05\x8a\x01\x02\x10\x00R\tcheckedAt\x12j\n\x0epermissionship\x18\x02 \x01(\x0e\x32\x36.authzed.api.v1.CheckPermissionResponse.PermissionshipB\n\xfa\x42\x07\x82\x01\x04\x10\x01 \x00R\x0epermissionship\x12[\n\x13partial_caveat_info\x18\x03 \x01(\x0b\x32!.authzed.api.v1.PartialCaveatInfoB\x08\xfa\x42\x05\x8a\x01\x02\x10\x00R\x11partialCaveatInfo\x12\x41\n\x0b\x64\x65\x62ug_trace\x18\x04 \x01(\x0b\x32 .authzed.api.v1.DebugInformationR\ndebugTrace\"\xa0\x01\n\x0ePermissionship\x12\x1e\n\x1aPERMISSIONSHIP_UNSPECIFIED\x10\x00\x12 \n\x1cPERMISSIONSHIP_NO_PERMISSION\x10\x01\x12!\n\x1dPERMISSIONSHIP_HAS_PERMISSION\x10\x02\x12)\n%PERMISSIONSHIP_CONDITIONAL_PERMISSION\x10\x03\"\xb2\x01\n\x1b\x43heckBulkPermissionsRequest\x12=\n\x0b\x63onsistency\x18\x01 \x01(\x0b\x32\x1b.authzed.api.v1.ConsistencyR\x0b\x63onsistency\x12T\n\x05items\x18\x02 \x03(\x0b\x32/.authzed.api.v1.CheckBulkPermissionsRequestItemB\r\xfa\x42\n\x92\x01\x07\"\x05\x8a\x01\x02\x10\x01R\x05items\"\xb7\x02\n\x1f\x43heckBulkPermissionsRequestItem\x12\x45\n\x08resource\x18\x01 \x01(\x0b\x32\x1f.authzed.api.v1.ObjectReferenceB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01R\x08resource\x12J\n\npermission\x18\x02 \x01(\tB*\xfa\x42\'r%(@2!^([a-z][a-z0-9_]{1,62}[a-z0-9])?$R\npermission\x12\x44\n\x07subject\x18\x03 \x01(\x0b\x32 .authzed.api.v1.SubjectReferenceB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01R\x07subject\x12;\n\x07\x63ontext\x18\x04 \x01(\x0b\x32\x17.google.protobuf.StructB\x08\xfa\x42\x05\x8a\x01\x02\x10\x00R\x07\x63ontext\"\xb0\x01\n\x1c\x43heckBulkPermissionsResponse\x12\x41\n\nchecked_at\x18\x01 \x01(\x0b\x32\x18.authzed.api.v1.ZedTokenB\x08\xfa\x42\x05\x8a\x01\x02\x10\x00R\tcheckedAt\x12M\n\x05pairs\x18\x02 \x03(\x0b\x32(.authzed.api.v1.CheckBulkPermissionsPairB\r\xfa\x42\n\x92\x01\x07\"\x05\x8a\x01\x02\x10\x01R\x05pairs\"\xe5\x01\n\x18\x43heckBulkPermissionsPair\x12I\n\x07request\x18\x01 \x01(\x0b\x32/.authzed.api.v1.CheckBulkPermissionsRequestItemR\x07request\x12\x46\n\x04item\x18\x02 \x01(\x0b\x32\x30.authzed.api.v1.CheckBulkPermissionsResponseItemH\x00R\x04item\x12*\n\x05\x65rror\x18\x03 \x01(\x0b\x32\x12.google.rpc.StatusH\x00R\x05\x65rrorB\n\n\x08response\"\xeb\x01\n CheckBulkPermissionsResponseItem\x12j\n\x0epermissionship\x18\x01 \x01(\x0e\x32\x36.authzed.api.v1.CheckPermissionResponse.PermissionshipB\n\xfa\x42\x07\x82\x01\x04\x10\x01 \x00R\x0epermissionship\x12[\n\x13partial_caveat_info\x18\x02 \x01(\x0b\x32!.authzed.api.v1.PartialCaveatInfoB\x08\xfa\x42\x05\x8a\x01\x02\x10\x00R\x11partialCaveatInfo\"\xef\x01\n\x1b\x45xpandPermissionTreeRequest\x12=\n\x0b\x63onsistency\x18\x01 \x01(\x0b\x32\x1b.authzed.api.v1.ConsistencyR\x0b\x63onsistency\x12\x45\n\x08resource\x18\x02 \x01(\x0b\x32\x1f.authzed.api.v1.ObjectReferenceB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01R\x08resource\x12J\n\npermission\x18\x03 \x01(\tB*\xfa\x42\'r%(@2!^([a-z][a-z0-9_]{1,62}[a-z0-9])?$R\npermission\"\xa2\x01\n\x1c\x45xpandPermissionTreeResponse\x12\x39\n\x0b\x65xpanded_at\x18\x01 \x01(\x0b\x32\x18.authzed.api.v1.ZedTokenR\nexpandedAt\x12G\n\ttree_root\x18\x02 \x01(\x0b\x32*.authzed.api.v1.PermissionRelationshipTreeR\x08treeRoot\"\x90\x04\n\x16LookupResourcesRequest\x12=\n\x0b\x63onsistency\x18\x01 \x01(\x0b\x32\x1b.authzed.api.v1.ConsistencyR\x0b\x63onsistency\x12z\n\x14resource_object_type\x18\x02 \x01(\tBH\xfa\x42\x45rC(\x80\x01\x32>^([a-z][a-z0-9_]{1,61}[a-z0-9]/)*[a-z][a-z0-9_]{1,62}[a-z0-9]$R\x12resourceObjectType\x12G\n\npermission\x18\x03 \x01(\tB\'\xfa\x42$r\"(@2\x1e^[a-z][a-z0-9_]{1,62}[a-z0-9]$R\npermission\x12\x44\n\x07subject\x18\x04 \x01(\x0b\x32 .authzed.api.v1.SubjectReferenceB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01R\x07subject\x12;\n\x07\x63ontext\x18\x05 \x01(\x0b\x32\x17.google.protobuf.StructB\x08\xfa\x42\x05\x8a\x01\x02\x10\x00R\x07\x63ontext\x12.\n\x0eoptional_limit\x18\x06 \x01(\rB\x07\xfa\x42\x04*\x02(\x00R\roptionalLimit\x12?\n\x0foptional_cursor\x18\x07 \x01(\x0b\x32\x16.authzed.api.v1.CursorR\x0eoptionalCursor\"\x82\x03\n\x17LookupResourcesResponse\x12:\n\x0clooked_up_at\x18\x01 \x01(\x0b\x32\x18.authzed.api.v1.ZedTokenR\nlookedUpAt\x12,\n\x12resource_object_id\x18\x02 \x01(\tR\x10resourceObjectId\x12X\n\x0epermissionship\x18\x03 \x01(\x0e\x32$.authzed.api.v1.LookupPermissionshipB\n\xfa\x42\x07\x82\x01\x04\x10\x01 \x00R\x0epermissionship\x12[\n\x13partial_caveat_info\x18\x04 \x01(\x0b\x32!.authzed.api.v1.PartialCaveatInfoB\x08\xfa\x42\x05\x8a\x01\x02\x10\x00R\x11partialCaveatInfo\x12\x46\n\x13\x61\x66ter_result_cursor\x18\x05 \x01(\x0b\x32\x16.authzed.api.v1.CursorR\x11\x61\x66terResultCursor\"\xea\x06\n\x15LookupSubjectsRequest\x12=\n\x0b\x63onsistency\x18\x01 \x01(\x0b\x32\x1b.authzed.api.v1.ConsistencyR\x0b\x63onsistency\x12\x45\n\x08resource\x18\x02 \x01(\x0b\x32\x1f.authzed.api.v1.ObjectReferenceB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01R\x08resource\x12J\n\npermission\x18\x03 \x01(\tB*\xfa\x42\'r%(@2!^([a-z][a-z0-9_]{1,62}[a-z0-9])?$R\npermission\x12x\n\x13subject_object_type\x18\x04 \x01(\tBH\xfa\x42\x45rC(\x80\x01\x32>^([a-z][a-z0-9_]{1,61}[a-z0-9]/)*[a-z][a-z0-9_]{1,62}[a-z0-9]$R\x11subjectObjectType\x12\x66\n\x19optional_subject_relation\x18\x05 \x01(\tB*\xfa\x42\'r%(@2!^([a-z][a-z0-9_]{1,62}[a-z0-9])?$R\x17optionalSubjectRelation\x12;\n\x07\x63ontext\x18\x06 \x01(\x0b\x32\x17.google.protobuf.StructB\x08\xfa\x42\x05\x8a\x01\x02\x10\x00R\x07\x63ontext\x12?\n\x17optional_concrete_limit\x18\x07 \x01(\rB\x07\xfa\x42\x04*\x02(\x00R\x15optionalConcreteLimit\x12?\n\x0foptional_cursor\x18\x08 \x01(\x0b\x32\x16.authzed.api.v1.CursorR\x0eoptionalCursor\x12]\n\x0fwildcard_option\x18\t \x01(\x0e\x32\x34.authzed.api.v1.LookupSubjectsRequest.WildcardOptionR\x0ewildcardOption\"\x7f\n\x0eWildcardOption\x12\x1f\n\x1bWILDCARD_OPTION_UNSPECIFIED\x10\x00\x12%\n!WILDCARD_OPTION_INCLUDE_WILDCARDS\x10\x01\x12%\n!WILDCARD_OPTION_EXCLUDE_WILDCARDS\x10\x02\"\xc6\x04\n\x16LookupSubjectsResponse\x12:\n\x0clooked_up_at\x18\x01 \x01(\x0b\x32\x18.authzed.api.v1.ZedTokenR\nlookedUpAt\x12.\n\x11subject_object_id\x18\x02 \x01(\tB\x02\x18\x01R\x0fsubjectObjectId\x12\x34\n\x14\x65xcluded_subject_ids\x18\x03 \x03(\tB\x02\x18\x01R\x12\x65xcludedSubjectIds\x12Z\n\x0epermissionship\x18\x04 \x01(\x0e\x32$.authzed.api.v1.LookupPermissionshipB\x0c\x18\x01\xfa\x42\x07\x82\x01\x04\x10\x01 \x00R\x0epermissionship\x12]\n\x13partial_caveat_info\x18\x05 \x01(\x0b\x32!.authzed.api.v1.PartialCaveatInfoB\n\x18\x01\xfa\x42\x05\x8a\x01\x02\x10\x00R\x11partialCaveatInfo\x12\x39\n\x07subject\x18\x06 \x01(\x0b\x32\x1f.authzed.api.v1.ResolvedSubjectR\x07subject\x12L\n\x11\x65xcluded_subjects\x18\x07 \x03(\x0b\x32\x1f.authzed.api.v1.ResolvedSubjectR\x10\x65xcludedSubjects\x12\x46\n\x13\x61\x66ter_result_cursor\x18\x08 \x01(\x0b\x32\x16.authzed.api.v1.CursorR\x11\x61\x66terResultCursor\"\xf4\x01\n\x0fResolvedSubject\x12*\n\x11subject_object_id\x18\x01 \x01(\tR\x0fsubjectObjectId\x12X\n\x0epermissionship\x18\x02 \x01(\x0e\x32$.authzed.api.v1.LookupPermissionshipB\n\xfa\x42\x07\x82\x01\x04\x10\x01 \x00R\x0epermissionship\x12[\n\x13partial_caveat_info\x18\x03 \x01(\x0b\x32!.authzed.api.v1.PartialCaveatInfoB\x08\xfa\x42\x05\x8a\x01\x02\x10\x00R\x11partialCaveatInfo*\x99\x01\n\x14LookupPermissionship\x12%\n!LOOKUP_PERMISSIONSHIP_UNSPECIFIED\x10\x00\x12(\n$LOOKUP_PERMISSIONSHIP_HAS_PERMISSION\x10\x01\x12\x30\n,LOOKUP_PERMISSIONSHIP_CONDITIONAL_PERMISSION\x10\x02\x32\x9a\t\n\x12PermissionsService\x12\x8d\x01\n\x11ReadRelationships\x12(.authzed.api.v1.ReadRelationshipsRequest\x1a).authzed.api.v1.ReadRelationshipsResponse\"!\x82\xd3\xe4\x93\x02\x1b\"\x16/v1/relationships/read:\x01*0\x01\x12\x8f\x01\n\x12WriteRelationships\x12).authzed.api.v1.WriteRelationshipsRequest\x1a*.authzed.api.v1.WriteRelationshipsResponse\"\"\x82\xd3\xe4\x93\x02\x1c\"\x17/v1/relationships/write:\x01*\x12\x93\x01\n\x13\x44\x65leteRelationships\x12*.authzed.api.v1.DeleteRelationshipsRequest\x1a+.authzed.api.v1.DeleteRelationshipsResponse\"#\x82\xd3\xe4\x93\x02\x1d\"\x18/v1/relationships/delete:\x01*\x12\x84\x01\n\x0f\x43heckPermission\x12&.authzed.api.v1.CheckPermissionRequest\x1a\'.authzed.api.v1.CheckPermissionResponse\" \x82\xd3\xe4\x93\x02\x1a\"\x15/v1/permissions/check:\x01*\x12\x97\x01\n\x14\x43heckBulkPermissions\x12+.authzed.api.v1.CheckBulkPermissionsRequest\x1a,.authzed.api.v1.CheckBulkPermissionsResponse\"$\x82\xd3\xe4\x93\x02\x1e\"\x19/v1/permissions/checkbulk:\x01*\x12\x94\x01\n\x14\x45xpandPermissionTree\x12+.authzed.api.v1.ExpandPermissionTreeRequest\x1a,.authzed.api.v1.ExpandPermissionTreeResponse\"!\x82\xd3\xe4\x93\x02\x1b\"\x16/v1/permissions/expand:\x01*\x12\x8a\x01\n\x0fLookupResources\x12&.authzed.api.v1.LookupResourcesRequest\x1a\'.authzed.api.v1.LookupResourcesResponse\"$\x82\xd3\xe4\x93\x02\x1e\"\x19/v1/permissions/resources:\x01*0\x01\x12\x86\x01\n\x0eLookupSubjects\x12%.authzed.api.v1.LookupSubjectsRequest\x1a&.authzed.api.v1.LookupSubjectsResponse\"#\x82\xd3\xe4\x93\x02\x1d\"\x18/v1/permissions/subjects:\x01*0\x01\x42J\n\x12\x63om.authzed.api.v1P\x01Z2github.com/authzed/authzed-go/proto/authzed/api/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'authzed.api.v1.permission_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\022com.authzed.api.v1P\001Z2github.com/authzed/authzed-go/proto/authzed/api/v1'
  _globals['_CONSISTENCY'].oneofs_by_name['requirement']._loaded_options = None
  _globals['_CONSISTENCY'].oneofs_by_name['requirement']._serialized_options = b'\370B\001'
  _globals['_CONSISTENCY'].fields_by_name['minimize_latency']._loaded_options = None
  _globals['_CONSISTENCY'].fields_by_name['minimize_latency']._serialized_options = b'\372B\004j\002\010\001'
  _globals['_CONSISTENCY'].fields_by_name['fully_consistent']._loaded_options = None
  _globals['_CONSISTENCY'].fields_by_name['fully_consistent']._serialized_options = b'\372B\004j\002\010\001'
  _globals['_RELATIONSHIPFILTER'].fields_by_name['resource_type']._loaded_options = None
  _globals['_RELATIONSHIPFILTER'].fields_by_name['resource_type']._serialized_options = b'\372BHrF(\200\0012A^(([a-z][a-z0-9_]{1,61}[a-z0-9]/)*[a-z][a-z0-9_]{1,62}[a-z0-9])?$'
  _globals['_RELATIONSHIPFILTER'].fields_by_name['optional_resource_id']._loaded_options = None
  _globals['_RELATIONSHIPFILTER'].fields_by_name['optional_resource_id']._serialized_options = b'\372B\"r (\200\0102\033^([a-zA-Z0-9/_|\\-=+]{1,})?$'
  _globals['_RELATIONSHIPFILTER'].fields_by_name['optional_resource_id_prefix']._loaded_options = None
  _globals['_RELATIONSHIPFILTER'].fields_by_name['optional_resource_id_prefix']._serialized_options = b'\372B\"r (\200\0102\033^([a-zA-Z0-9/_|\\-=+]{1,})?$'
  _globals['_RELATIONSHIPFILTER'].fields_by_name['optional_relation']._loaded_options = None
  _globals['_RELATIONSHIPFILTER'].fields_by_name['optional_relation']._serialized_options = b'\372B\'r%(@2!^([a-z][a-z0-9_]{1,62}[a-z0-9])?$'
  _globals['_SUBJECTFILTER_RELATIONFILTER'].fields_by_name['relation']._loaded_options = None
  _globals['_SUBJECTFILTER_RELATIONFILTER'].fields_by_name['relation']._serialized_options = b'\372B\'r%(@2!^([a-z][a-z0-9_]{1,62}[a-z0-9])?$'
  _globals['_SUBJECTFILTER'].fields_by_name['subject_type']._loaded_options = None
  _globals['_SUBJECTFILTER'].fields_by_name['subject_type']._serialized_options = b'\372BErC(\200\0012>^([a-z][a-z0-9_]{1,61}[a-z0-9]/)*[a-z][a-z0-9_]{1,62}[a-z0-9]$'
  _globals['_SUBJECTFILTER'].fields_by_name['optional_subject_id']._loaded_options = None
  _globals['_SUBJECTFILTER'].fields_by_name['optional_subject_id']._serialized_options = b'\372B\'r%(\200\0102 ^(([a-zA-Z0-9/_|\\-=+]{1,})|\\*)?$'
  _globals['_READRELATIONSHIPSREQUEST'].fields_by_name['relationship_filter']._loaded_options = None
  _globals['_READRELATIONSHIPSREQUEST'].fields_by_name['relationship_filter']._serialized_options = b'\372B\005\212\001\002\020\001'
  _globals['_READRELATIONSHIPSREQUEST'].fields_by_name['optional_limit']._loaded_options = None
  _globals['_READRELATIONSHIPSREQUEST'].fields_by_name['optional_limit']._serialized_options = b'\372B\004*\002(\000'
  _globals['_READRELATIONSHIPSRESPONSE'].fields_by_name['read_at']._loaded_options = None
  _globals['_READRELATIONSHIPSRESPONSE'].fields_by_name['read_at']._serialized_options = b'\372B\005\212\001\002\020\001'
  _globals['_READRELATIONSHIPSRESPONSE'].fields_by_name['relationship']._loaded_options = None
  _globals['_READRELATIONSHIPSRESPONSE'].fields_by_name['relationship']._serialized_options = b'\372B\005\212\001\002\020\001'
  _globals['_PRECONDITION'].fields_by_name['operation']._loaded_options = None
  _globals['_PRECONDITION'].fields_by_name['operation']._serialized_options = b'\372B\007\202\001\004\020\001 \000'
  _globals['_PRECONDITION'].fields_by_name['filter']._loaded_options = None
  _globals['_PRECONDITION'].fields_by_name['filter']._serialized_options = b'\372B\005\212\001\002\020\001'
  _globals['_WRITERELATIONSHIPSREQUEST'].fields_by_name['updates']._loaded_options = None
  _globals['_WRITERELATIONSHIPSREQUEST'].fields_by_name['updates']._serialized_options = b'\372B\n\222\001\007\"\005\212\001\002\020\001'
  _globals['_WRITERELATIONSHIPSREQUEST'].fields_by_name['optional_preconditions']._loaded_options = None
  _globals['_WRITERELATIONSHIPSREQUEST'].fields_by_name['optional_preconditions']._serialized_options = b'\372B\n\222\001\007\"\005\212\001\002\020\001'
  _globals['_DELETERELATIONSHIPSREQUEST'].fields_by_name['relationship_filter']._loaded_options = None
  _globals['_DELETERELATIONSHIPSREQUEST'].fields_by_name['relationship_filter']._serialized_options = b'\372B\005\212\001\002\020\001'
  _globals['_DELETERELATIONSHIPSREQUEST'].fields_by_name['optional_preconditions']._loaded_options = None
  _globals['_DELETERELATIONSHIPSREQUEST'].fields_by_name['optional_preconditions']._serialized_options = b'\372B\n\222\001\007\"\005\212\001\002\020\001'
  _globals['_DELETERELATIONSHIPSREQUEST'].fields_by_name['optional_limit']._loaded_options = None
  _globals['_DELETERELATIONSHIPSREQUEST'].fields_by_name['optional_limit']._serialized_options = b'\372B\004*\002(\000'
  _globals['_CHECKPERMISSIONREQUEST'].fields_by_name['resource']._loaded_options = None
  _globals['_CHECKPERMISSIONREQUEST'].fields_by_name['resource']._serialized_options = b'\372B\005\212\001\002\020\001'
  _globals['_CHECKPERMISSIONREQUEST'].fields_by_name['permission']._loaded_options = None
  _globals['_CHECKPERMISSIONREQUEST'].fields_by_name['permission']._serialized_options = b'\372B\'r%(@2!^([a-z][a-z0-9_]{1,62}[a-z0-9])?$'
  _globals['_CHECKPERMISSIONREQUEST'].fields_by_name['subject']._loaded_options = None
  _globals['_CHECKPERMISSIONREQUEST'].fields_by_name['subject']._serialized_options = b'\372B\005\212\001\002\020\001'
  _globals['_CHECKPERMISSIONREQUEST'].fields_by_name['context']._loaded_options = None
  _globals['_CHECKPERMISSIONREQUEST'].fields_by_name['context']._serialized_options = b'\372B\005\212\001\002\020\000'
  _globals['_CHECKPERMISSIONRESPONSE'].fields_by_name['checked_at']._loaded_options = None
  _globals['_CHECKPERMISSIONRESPONSE'].fields_by_name['checked_at']._serialized_options = b'\372B\005\212\001\002\020\000'
  _globals['_CHECKPERMISSIONRESPONSE'].fields_by_name['permissionship']._loaded_options = None
  _globals['_CHECKPERMISSIONRESPONSE'].fields_by_name['permissionship']._serialized_options = b'\372B\007\202\001\004\020\001 \000'
  _globals['_CHECKPERMISSIONRESPONSE'].fields_by_name['partial_caveat_info']._loaded_options = None
  _globals['_CHECKPERMISSIONRESPONSE'].fields_by_name['partial_caveat_info']._serialized_options = b'\372B\005\212\001\002\020\000'
  _globals['_CHECKBULKPERMISSIONSREQUEST'].fields_by_name['items']._loaded_options = None
  _globals['_CHECKBULKPERMISSIONSREQUEST'].fields_by_name['items']._serialized_options = b'\372B\n\222\001\007\"\005\212\001\002\020\001'
  _globals['_CHECKBULKPERMISSIONSREQUESTITEM'].fields_by_name['resource']._loaded_options = None
  _globals['_CHECKBULKPERMISSIONSREQUESTITEM'].fields_by_name['resource']._serialized_options = b'\372B\005\212\001\002\020\001'
  _globals['_CHECKBULKPERMISSIONSREQUESTITEM'].fields_by_name['permission']._loaded_options = None
  _globals['_CHECKBULKPERMISSIONSREQUESTITEM'].fields_by_name['permission']._serialized_options = b'\372B\'r%(@2!^([a-z][a-z0-9_]{1,62}[a-z0-9])?$'
  _globals['_CHECKBULKPERMISSIONSREQUESTITEM'].fields_by_name['subject']._loaded_options = None
  _globals['_CHECKBULKPERMISSIONSREQUESTITEM'].fields_by_name['subject']._serialized_options = b'\372B\005\212\001\002\020\001'
  _globals['_CHECKBULKPERMISSIONSREQUESTITEM'].fields_by_name['context']._loaded_options = None
  _globals['_CHECKBULKPERMISSIONSREQUESTITEM'].fields_by_name['context']._serialized_options = b'\372B\005\212\001\002\020\000'
  _globals['_CHECKBULKPERMISSIONSRESPONSE'].fields_by_name['checked_at']._loaded_options = None
  _globals['_CHECKBULKPERMISSIONSRESPONSE'].fields_by_name['checked_at']._serialized_options = b'\372B\005\212\001\002\020\000'
  _globals['_CHECKBULKPERMISSIONSRESPONSE'].fields_by_name['pairs']._loaded_options = None
  _globals['_CHECKBULKPERMISSIONSRESPONSE'].fields_by_name['pairs']._serialized_options = b'\372B\n\222\001\007\"\005\212\001\002\020\001'
  _globals['_CHECKBULKPERMISSIONSRESPONSEITEM'].fields_by_name['permissionship']._loaded_options = None
  _globals['_CHECKBULKPERMISSIONSRESPONSEITEM'].fields_by_name['permissionship']._serialized_options = b'\372B\007\202\001\004\020\001 \000'
  _globals['_CHECKBULKPERMISSIONSRESPONSEITEM'].fields_by_name['partial_caveat_info']._loaded_options = None
  _globals['_CHECKBULKPERMISSIONSRESPONSEITEM'].fields_by_name['partial_caveat_info']._serialized_options = b'\372B\005\212\001\002\020\000'
  _globals['_EXPANDPERMISSIONTREEREQUEST'].fields_by_name['resource']._loaded_options = None
  _globals['_EXPANDPERMISSIONTREEREQUEST'].fields_by_name['resource']._serialized_options = b'\372B\005\212\001\002\020\001'
  _globals['_EXPANDPERMISSIONTREEREQUEST'].fields_by_name['permission']._loaded_options = None
  _globals['_EXPANDPERMISSIONTREEREQUEST'].fields_by_name['permission']._serialized_options = b'\372B\'r%(@2!^([a-z][a-z0-9_]{1,62}[a-z0-9])?$'
  _globals['_LOOKUPRESOURCESREQUEST'].fields_by_name['resource_object_type']._loaded_options = None
  _globals['_LOOKUPRESOURCESREQUEST'].fields_by_name['resource_object_type']._serialized_options = b'\372BErC(\200\0012>^([a-z][a-z0-9_]{1,61}[a-z0-9]/)*[a-z][a-z0-9_]{1,62}[a-z0-9]$'
  _globals['_LOOKUPRESOURCESREQUEST'].fields_by_name['permission']._loaded_options = None
  _globals['_LOOKUPRESOURCESREQUEST'].fields_by_name['permission']._serialized_options = b'\372B$r\"(@2\036^[a-z][a-z0-9_]{1,62}[a-z0-9]$'
  _globals['_LOOKUPRESOURCESREQUEST'].fields_by_name['subject']._loaded_options = None
  _globals['_LOOKUPRESOURCESREQUEST'].fields_by_name['subject']._serialized_options = b'\372B\005\212\001\002\020\001'
  _globals['_LOOKUPRESOURCESREQUEST'].fields_by_name['context']._loaded_options = None
  _globals['_LOOKUPRESOURCESREQUEST'].fields_by_name['context']._serialized_options = b'\372B\005\212\001\002\020\000'
  _globals['_LOOKUPRESOURCESREQUEST'].fields_by_name['optional_limit']._loaded_options = None
  _globals['_LOOKUPRESOURCESREQUEST'].fields_by_name['optional_limit']._serialized_options = b'\372B\004*\002(\000'
  _globals['_LOOKUPRESOURCESRESPONSE'].fields_by_name['permissionship']._loaded_options = None
  _globals['_LOOKUPRESOURCESRESPONSE'].fields_by_name['permissionship']._serialized_options = b'\372B\007\202\001\004\020\001 \000'
  _globals['_LOOKUPRESOURCESRESPONSE'].fields_by_name['partial_caveat_info']._loaded_options = None
  _globals['_LOOKUPRESOURCESRESPONSE'].fields_by_name['partial_caveat_info']._serialized_options = b'\372B\005\212\001\002\020\000'
  _globals['_LOOKUPSUBJECTSREQUEST'].fields_by_name['resource']._loaded_options = None
  _globals['_LOOKUPSUBJECTSREQUEST'].fields_by_name['resource']._serialized_options = b'\372B\005\212\001\002\020\001'
  _globals['_LOOKUPSUBJECTSREQUEST'].fields_by_name['permission']._loaded_options = None
  _globals['_LOOKUPSUBJECTSREQUEST'].fields_by_name['permission']._serialized_options = b'\372B\'r%(@2!^([a-z][a-z0-9_]{1,62}[a-z0-9])?$'
  _globals['_LOOKUPSUBJECTSREQUEST'].fields_by_name['subject_object_type']._loaded_options = None
  _globals['_LOOKUPSUBJECTSREQUEST'].fields_by_name['subject_object_type']._serialized_options = b'\372BErC(\200\0012>^([a-z][a-z0-9_]{1,61}[a-z0-9]/)*[a-z][a-z0-9_]{1,62}[a-z0-9]$'
  _globals['_LOOKUPSUBJECTSREQUEST'].fields_by_name['optional_subject_relation']._loaded_options = None
  _globals['_LOOKUPSUBJECTSREQUEST'].fields_by_name['optional_subject_relation']._serialized_options = b'\372B\'r%(@2!^([a-z][a-z0-9_]{1,62}[a-z0-9])?$'
  _globals['_LOOKUPSUBJECTSREQUEST'].fields_by_name['context']._loaded_options = None
  _globals['_LOOKUPSUBJECTSREQUEST'].fields_by_name['context']._serialized_options = b'\372B\005\212\001\002\020\000'
  _globals['_LOOKUPSUBJECTSREQUEST'].fields_by_name['optional_concrete_limit']._loaded_options = None
  _globals['_LOOKUPSUBJECTSREQUEST'].fields_by_name['optional_concrete_limit']._serialized_options = b'\372B\004*\002(\000'
  _globals['_LOOKUPSUBJECTSRESPONSE'].fields_by_name['subject_object_id']._loaded_options = None
  _globals['_LOOKUPSUBJECTSRESPONSE'].fields_by_name['subject_object_id']._serialized_options = b'\030\001'
  _globals['_LOOKUPSUBJECTSRESPONSE'].fields_by_name['excluded_subject_ids']._loaded_options = None
  _globals['_LOOKUPSUBJECTSRESPONSE'].fields_by_name['excluded_subject_ids']._serialized_options = b'\030\001'
  _globals['_LOOKUPSUBJECTSRESPONSE'].fields_by_name['permissionship']._loaded_options = None
  _globals['_LOOKUPSUBJECTSRESPONSE'].fields_by_name['permissionship']._serialized_options = b'\030\001\372B\007\202\001\004\020\001 \000'
  _globals['_LOOKUPSUBJECTSRESPONSE'].fields_by_name['partial_caveat_info']._loaded_options = None
  _globals['_LOOKUPSUBJECTSRESPONSE'].fields_by_name['partial_caveat_info']._serialized_options = b'\030\001\372B\005\212\001\002\020\000'
  _globals['_RESOLVEDSUBJECT'].fields_by_name['permissionship']._loaded_options = None
  _globals['_RESOLVEDSUBJECT'].fields_by_name['permissionship']._serialized_options = b'\372B\007\202\001\004\020\001 \000'
  _globals['_RESOLVEDSUBJECT'].fields_by_name['partial_caveat_info']._loaded_options = None
  _globals['_RESOLVEDSUBJECT'].fields_by_name['partial_caveat_info']._serialized_options = b'\372B\005\212\001\002\020\000'
  _globals['_PERMISSIONSSERVICE'].methods_by_name['ReadRelationships']._loaded_options = None
  _globals['_PERMISSIONSSERVICE'].methods_by_name['ReadRelationships']._serialized_options = b'\202\323\344\223\002\033\"\026/v1/relationships/read:\001*'
  _globals['_PERMISSIONSSERVICE'].methods_by_name['WriteRelationships']._loaded_options = None
  _globals['_PERMISSIONSSERVICE'].methods_by_name['WriteRelationships']._serialized_options = b'\202\323\344\223\002\034\"\027/v1/relationships/write:\001*'
  _globals['_PERMISSIONSSERVICE'].methods_by_name['DeleteRelationships']._loaded_options = None
  _globals['_PERMISSIONSSERVICE'].methods_by_name['DeleteRelationships']._serialized_options = b'\202\323\344\223\002\035\"\030/v1/relationships/delete:\001*'
  _globals['_PERMISSIONSSERVICE'].methods_by_name['CheckPermission']._loaded_options = None
  _globals['_PERMISSIONSSERVICE'].methods_by_name['CheckPermission']._serialized_options = b'\202\323\344\223\002\032\"\025/v1/permissions/check:\001*'
  _globals['_PERMISSIONSSERVICE'].methods_by_name['CheckBulkPermissions']._loaded_options = None
  _globals['_PERMISSIONSSERVICE'].methods_by_name['CheckBulkPermissions']._serialized_options = b'\202\323\344\223\002\036\"\031/v1/permissions/checkbulk:\001*'
  _globals['_PERMISSIONSSERVICE'].methods_by_name['ExpandPermissionTree']._loaded_options = None
  _globals['_PERMISSIONSSERVICE'].methods_by_name['ExpandPermissionTree']._serialized_options = b'\202\323\344\223\002\033\"\026/v1/permissions/expand:\001*'
  _globals['_PERMISSIONSSERVICE'].methods_by_name['LookupResources']._loaded_options = None
  _globals['_PERMISSIONSSERVICE'].methods_by_name['LookupResources']._serialized_options = b'\202\323\344\223\002\036\"\031/v1/permissions/resources:\001*'
  _globals['_PERMISSIONSSERVICE'].methods_by_name['LookupSubjects']._loaded_options = None
  _globals['_PERMISSIONSSERVICE'].methods_by_name['LookupSubjects']._serialized_options = b'\202\323\344\223\002\035\"\030/v1/permissions/subjects:\001*'
  _globals['_LOOKUPPERMISSIONSHIP']._serialized_start=8284
  _globals['_LOOKUPPERMISSIONSHIP']._serialized_end=8437
  _globals['_CONSISTENCY']._serialized_start=225
  _globals['_CONSISTENCY']._serialized_end=509
  _globals['_RELATIONSHIPFILTER']._serialized_start=512
  _globals['_RELATIONSHIPFILTER']._serialized_end=1013
  _globals['_SUBJECTFILTER']._serialized_start=1016
  _globals['_SUBJECTFILTER']._serialized_end=1413
  _globals['_SUBJECTFILTER_RELATIONFILTER']._serialized_start=1325
  _globals['_SUBJECTFILTER_RELATIONFILTER']._serialized_end=1413
  _globals['_READRELATIONSHIPSREQUEST']._serialized_start=1416
  _globals['_READRELATIONSHIPSREQUEST']._serialized_end=1713
  _globals['_READRELATIONSHIPSRESPONSE']._serialized_start=1716
  _globals['_READRELATIONSHIPSRESPONSE']._serialized_end=1952
  _globals['_PRECONDITION']._serialized_start=1955
  _globals['_PRECONDITION']._serialized_end=2217
  _globals['_PRECONDITION_OPERATION']._serialized_start=2123
  _globals['_PRECONDITION_OPERATION']._serialized_end=2217
  _globals['_WRITERELATIONSHIPSREQUEST']._serialized_start=2220
  _globals['_WRITERELATIONSHIPSREQUEST']._serialized_end=2424
  _globals['_WRITERELATIONSHIPSRESPONSE']._serialized_start=2426
  _globals['_WRITERELATIONSHIPSRESPONSE']._serialized_end=2511
  _globals['_DELETERELATIONSHIPSREQUEST']._serialized_start=2514
  _globals['_DELETERELATIONSHIPSREQUEST']._serialized_end=2858
  _globals['_DELETERELATIONSHIPSRESPONSE']._serialized_start=2861
  _globals['_DELETERELATIONSHIPSRESPONSE']._serialized_end=3172
  _globals['_DELETERELATIONSHIPSRESPONSE_DELETIONPROGRESS']._serialized_start=3056
  _globals['_DELETERELATIONSHIPSRESPONSE_DELETIONPROGRESS']._serialized_end=3172
  _globals['_CHECKPERMISSIONREQUEST']._serialized_start=3175
  _globals['_CHECKPERMISSIONREQUEST']._serialized_end=3575
  _globals['_CHECKPERMISSIONRESPONSE']._serialized_start=3578
  _globals['_CHECKPERMISSIONRESPONSE']._serialized_end=4101
  _globals['_CHECKPERMISSIONRESPONSE_PERMISSIONSHIP']._serialized_start=3941
  _globals['_CHECKPERMISSIONRESPONSE_PERMISSIONSHIP']._serialized_end=4101
  _globals['_CHECKBULKPERMISSIONSREQUEST']._serialized_start=4104
  _globals['_CHECKBULKPERMISSIONSREQUEST']._serialized_end=4282
  _globals['_CHECKBULKPERMISSIONSREQUESTITEM']._serialized_start=4285
  _globals['_CHECKBULKPERMISSIONSREQUESTITEM']._serialized_end=4596
  _globals['_CHECKBULKPERMISSIONSRESPONSE']._serialized_start=4599
  _globals['_CHECKBULKPERMISSIONSRESPONSE']._serialized_end=4775
  _globals['_CHECKBULKPERMISSIONSPAIR']._serialized_start=4778
  _globals['_CHECKBULKPERMISSIONSPAIR']._serialized_end=5007
  _globals['_CHECKBULKPERMISSIONSRESPONSEITEM']._serialized_start=5010
  _globals['_CHECKBULKPERMISSIONSRESPONSEITEM']._serialized_end=5245
  _globals['_EXPANDPERMISSIONTREEREQUEST']._serialized_start=5248
  _globals['_EXPANDPERMISSIONTREEREQUEST']._serialized_end=5487
  _globals['_EXPANDPERMISSIONTREERESPONSE']._serialized_start=5490
  _globals['_EXPANDPERMISSIONTREERESPONSE']._serialized_end=5652
  _globals['_LOOKUPRESOURCESREQUEST']._serialized_start=5655
  _globals['_LOOKUPRESOURCESREQUEST']._serialized_end=6183
  _globals['_LOOKUPRESOURCESRESPONSE']._serialized_start=6186
  _globals['_LOOKUPRESOURCESRESPONSE']._serialized_end=6572
  _globals['_LOOKUPSUBJECTSREQUEST']._serialized_start=6575
  _globals['_LOOKUPSUBJECTSREQUEST']._serialized_end=7449
  _globals['_LOOKUPSUBJECTSREQUEST_WILDCARDOPTION']._serialized_start=7322
  _globals['_LOOKUPSUBJECTSREQUEST_WILDCARDOPTION']._serialized_end=7449
  _globals['_LOOKUPSUBJECTSRESPONSE']._serialized_start=7452
  _globals['_LOOKUPSUBJECTSRESPONSE']._serialized_end=8034
  _globals['_RESOLVEDSUBJECT']._serialized_start=8037
  _globals['_RESOLVEDSUBJECT']._serialized_end=8281
  _globals['_PERMISSIONSSERVICE']._serialized_start=8440
  _globals['_PERMISSIONSSERVICE']._serialized_end=9618
# @@protoc_insertion_point(module_scope)
