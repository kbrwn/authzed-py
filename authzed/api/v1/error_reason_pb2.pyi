"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _ErrorReason:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _ErrorReasonEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ErrorReason.ValueType], builtins.type):  # noqa: F821
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    ERROR_REASON_UNSPECIFIED: _ErrorReason.ValueType  # 0
    """Do not use this default value."""
    ERROR_REASON_SCHEMA_PARSE_ERROR: _ErrorReason.ValueType  # 1
    """The request gave a schema that could not be parsed.

    Example of an ErrorInfo:

        { 
          "reason": "ERROR_REASON_SCHEMA_PARSE_ERROR",
          "domain": "authzed.com",
          "metadata": {
            "start_line_number": "1",
            "start_column_position": "19",
            "end_line_number": "1",
            "end_column_position": "19",
            "source_code": "somedefinition",
          }
        }

    The line numbers and column positions are 0-indexed and may not be present.
    """
    ERROR_REASON_SCHEMA_TYPE_ERROR: _ErrorReason.ValueType  # 2
    """The request contains a schema with a type error.

    Example of an ErrorInfo:

        {  
          "reason": "ERROR_REASON_SCHEMA_TYPE_ERROR",
          "domain": "authzed.com",
          "metadata": {
            "definition_name": "somedefinition",
            ... additional keys based on the kind of type error ...
          }
        }
    """
    ERROR_REASON_UNKNOWN_DEFINITION: _ErrorReason.ValueType  # 3
    """The request referenced an unknown object definition in the schema.

    Example of an ErrorInfo:

        {  
          "reason": "ERROR_REASON_UNKNOWN_DEFINITION",
          "domain": "authzed.com",
          "metadata": {
            "definition_name": "somedefinition"
          }
        }
    """
    ERROR_REASON_UNKNOWN_RELATION_OR_PERMISSION: _ErrorReason.ValueType  # 4
    """The request referenced an unknown relation or permission under a definition in the schema.

    Example of an ErrorInfo:

        {  
          "reason": "ERROR_REASON_UNKNOWN_RELATION_OR_PERMISSION",
          "domain": "authzed.com",
          "metadata": {
            "definition_name": "somedefinition",
            "relation_or_permission_name": "somepermission"
          }
        }
    """
    ERROR_REASON_TOO_MANY_UPDATES_IN_REQUEST: _ErrorReason.ValueType  # 5
    """The WriteRelationships request contained more updates than the maximum configured.

    Example of an ErrorInfo:

        { "reason": "ERROR_REASON_TOO_MANY_UPDATES_IN_REQUEST",
          "domain": "authzed.com",
          "metadata": {
            "update_count": "525",
            "maximum_updates_allowed": "500",
          }
        }
    """
    ERROR_REASON_TOO_MANY_PRECONDITIONS_IN_REQUEST: _ErrorReason.ValueType  # 6
    """The request contained more preconditions than the maximum configured.

    Example of an ErrorInfo:

        {  
          "reason": "ERROR_REASON_TOO_MANY_PRECONDITIONS_IN_REQUEST",
          "domain": "authzed.com",
          "metadata": {
            "precondition_count": "525",
            "maximum_preconditions_allowed": "500",
          }
        }
    """
    ERROR_REASON_WRITE_OR_DELETE_PRECONDITION_FAILURE: _ErrorReason.ValueType  # 7
    """The request contained a precondition that failed.

    Example of an ErrorInfo:

        {  
          "reason": "ERROR_REASON_WRITE_OR_DELETE_PRECONDITION_FAILURE",
          "domain": "authzed.com",
          "metadata": {
            "precondition_resource_type": "document",
            ... other fields for the filter ...
            "precondition_operation": "MUST_EXIST",
          }
        }
    """
    ERROR_REASON_SERVICE_READ_ONLY: _ErrorReason.ValueType  # 8
    """A write or delete request was made to an instance that is deployed in read-only mode.

    Example of an ErrorInfo:

        {  
          "reason": "ERROR_REASON_SERVICE_READ_ONLY",
          "domain": "authzed.com"
        }
    """
    ERROR_REASON_UNKNOWN_CAVEAT: _ErrorReason.ValueType  # 9
    """The request referenced an unknown caveat in the schema.

    Example of an ErrorInfo:

        {  
          "reason": "ERROR_REASON_UNKNOWN_CAVEAT",
          "domain": "authzed.com",
          "metadata": {
            "caveat_name": "somecaveat"
          }
        }
    """
    ERROR_REASON_INVALID_SUBJECT_TYPE: _ErrorReason.ValueType  # 10
    """The request tries to use a subject type that was not valid for a relation.

    Example of an ErrorInfo:

        {  
          "reason": "ERROR_REASON_INVALID_SUBJECT_TYPE",
          "domain": "authzed.com",
          "metadata": {
            "definition_name": "somedefinition",
            "relation_name": "somerelation",
            "subject_type": "user:*"
          }
        }
    """
    ERROR_REASON_CAVEAT_PARAMETER_TYPE_ERROR: _ErrorReason.ValueType  # 11
    """The request tries to specify a caveat parameter value with the wrong type.

    Example of an ErrorInfo:

        {  
          "reason": "ERROR_REASON_CAVEAT_PARAMETER_TYPE_ERROR",
          "domain": "authzed.com",
          "metadata": {
            "definition_name": "somedefinition",
            "relation_name": "somerelation",
            "caveat_name": "somecaveat",
            "parameter_name": "someparameter",
            "expected_type": "int",
          }
        }
    """
    ERROR_REASON_UPDATES_ON_SAME_RELATIONSHIP: _ErrorReason.ValueType  # 12
    """The request tries to perform two or more updates on the same relationship in the same WriteRelationships call.

    Example of an ErrorInfo:

        {  
          "reason": "ERROR_REASON_UPDATES_ON_SAME_RELATIONSHIP",
          "domain": "authzed.com",
          "metadata": {
            "definition_name": "somedefinition",
            "relationship": "somerelationship",
          }
        }
    """
    ERROR_REASON_CANNOT_UPDATE_PERMISSION: _ErrorReason.ValueType  # 13
    """The request tries to write a relationship on a permission instead of a relation.

    Example of an ErrorInfo:

        {  
          "reason": "ERROR_REASON_CANNOT_UPDATE_PERMISSION",
          "domain": "authzed.com",
          "metadata": {
            "definition_name": "somedefinition",
            "permission_name": "somerelation",
          }
        }
    """
    ERROR_REASON_CAVEAT_EVALUATION_ERROR: _ErrorReason.ValueType  # 14
    """The request failed to evaluate a caveat expression due to an error.

    Example of an ErrorInfo:

        {  
          "reason": "ERROR_REASON_CAVEAT_EVALUATION_ERROR",
          "domain": "authzed.com",
          "metadata": {
            "caveat_name": "somecaveat",
          }
        }
    """
    ERROR_REASON_INVALID_CURSOR: _ErrorReason.ValueType  # 15
    """The request failed because the provided cursor was invalid in some way.

    Example of an ErrorInfo:

        {  
          "reason": "ERROR_REASON_INVALID_CURSOR",
          "domain": "authzed.com",
          "metadata": {
             ... additional keys based on the kind of cursor error ...
          }
        }
    """
    ERROR_REASON_TOO_MANY_RELATIONSHIPS_FOR_TRANSACTIONAL_DELETE: _ErrorReason.ValueType  # 16
    """The request failed because there are too many matching relationships to be
    deleted within a single transactional deletion call. To avoid, set
    `optional_allow_partial_deletions` to true on the DeleteRelationships call.

    Example of an ErrorInfo:

        {  
          "reason": "ERROR_REASON_TOO_MANY_RELATIONSHIPS_FOR_TRANSACTIONAL_DELETE",
          "domain": "authzed.com",
          "metadata": {
             ... fields for the filter ...
          }
        }
    """
    ERROR_REASON_MAX_RELATIONSHIP_CONTEXT_SIZE: _ErrorReason.ValueType  # 17
    """The request failed because the client attempted to write a relationship
    with a context that exceeded the configured server limit.

    Example of an ErrorInfo:

        {
          "reason": "ERROR_REASON_MAX_RELATIONSHIP_CONTEXT_SIZE",
          "domain": "authzed.com",
          "metadata": {
            "relationship":     "relationship_exceeding_the_limit",
            "max_allowed_size": "server_max_allowed_context_size",
            "context_size":     "actual_relationship_context_size" ,
          }
        }
    """
    ERROR_REASON_ATTEMPT_TO_RECREATE_RELATIONSHIP: _ErrorReason.ValueType  # 18
    """The request failed because a relationship marked to be CREATEd
    was already present within the datastore.

    Example of an ErrorInfo:

        {
          "reason": "ERROR_REASON_ATTEMPT_TO_RECREATE_RELATIONSHIP",
          "domain": "authzed.com",
          "metadata": {
            "relationship":          "relationship_that_already_existed",
            "resource_type":         "resource type",
            "resource_object_id":    "resource object id",
            ... additional decomposed relationship fields ...
          }
        }
    """

class ErrorReason(_ErrorReason, metaclass=_ErrorReasonEnumTypeWrapper):
    """Defines the supported values for `google.rpc.ErrorInfo.reason` for the
    `authzed.com` error domain.
    """

ERROR_REASON_UNSPECIFIED: ErrorReason.ValueType  # 0
"""Do not use this default value."""
ERROR_REASON_SCHEMA_PARSE_ERROR: ErrorReason.ValueType  # 1
"""The request gave a schema that could not be parsed.

Example of an ErrorInfo:

    { 
      "reason": "ERROR_REASON_SCHEMA_PARSE_ERROR",
      "domain": "authzed.com",
      "metadata": {
        "start_line_number": "1",
        "start_column_position": "19",
        "end_line_number": "1",
        "end_column_position": "19",
        "source_code": "somedefinition",
      }
    }

The line numbers and column positions are 0-indexed and may not be present.
"""
ERROR_REASON_SCHEMA_TYPE_ERROR: ErrorReason.ValueType  # 2
"""The request contains a schema with a type error.

Example of an ErrorInfo:

    {  
      "reason": "ERROR_REASON_SCHEMA_TYPE_ERROR",
      "domain": "authzed.com",
      "metadata": {
        "definition_name": "somedefinition",
        ... additional keys based on the kind of type error ...
      }
    }
"""
ERROR_REASON_UNKNOWN_DEFINITION: ErrorReason.ValueType  # 3
"""The request referenced an unknown object definition in the schema.

Example of an ErrorInfo:

    {  
      "reason": "ERROR_REASON_UNKNOWN_DEFINITION",
      "domain": "authzed.com",
      "metadata": {
        "definition_name": "somedefinition"
      }
    }
"""
ERROR_REASON_UNKNOWN_RELATION_OR_PERMISSION: ErrorReason.ValueType  # 4
"""The request referenced an unknown relation or permission under a definition in the schema.

Example of an ErrorInfo:

    {  
      "reason": "ERROR_REASON_UNKNOWN_RELATION_OR_PERMISSION",
      "domain": "authzed.com",
      "metadata": {
        "definition_name": "somedefinition",
        "relation_or_permission_name": "somepermission"
      }
    }
"""
ERROR_REASON_TOO_MANY_UPDATES_IN_REQUEST: ErrorReason.ValueType  # 5
"""The WriteRelationships request contained more updates than the maximum configured.

Example of an ErrorInfo:

    { "reason": "ERROR_REASON_TOO_MANY_UPDATES_IN_REQUEST",
      "domain": "authzed.com",
      "metadata": {
        "update_count": "525",
        "maximum_updates_allowed": "500",
      }
    }
"""
ERROR_REASON_TOO_MANY_PRECONDITIONS_IN_REQUEST: ErrorReason.ValueType  # 6
"""The request contained more preconditions than the maximum configured.

Example of an ErrorInfo:

    {  
      "reason": "ERROR_REASON_TOO_MANY_PRECONDITIONS_IN_REQUEST",
      "domain": "authzed.com",
      "metadata": {
        "precondition_count": "525",
        "maximum_preconditions_allowed": "500",
      }
    }
"""
ERROR_REASON_WRITE_OR_DELETE_PRECONDITION_FAILURE: ErrorReason.ValueType  # 7
"""The request contained a precondition that failed.

Example of an ErrorInfo:

    {  
      "reason": "ERROR_REASON_WRITE_OR_DELETE_PRECONDITION_FAILURE",
      "domain": "authzed.com",
      "metadata": {
        "precondition_resource_type": "document",
        ... other fields for the filter ...
        "precondition_operation": "MUST_EXIST",
      }
    }
"""
ERROR_REASON_SERVICE_READ_ONLY: ErrorReason.ValueType  # 8
"""A write or delete request was made to an instance that is deployed in read-only mode.

Example of an ErrorInfo:

    {  
      "reason": "ERROR_REASON_SERVICE_READ_ONLY",
      "domain": "authzed.com"
    }
"""
ERROR_REASON_UNKNOWN_CAVEAT: ErrorReason.ValueType  # 9
"""The request referenced an unknown caveat in the schema.

Example of an ErrorInfo:

    {  
      "reason": "ERROR_REASON_UNKNOWN_CAVEAT",
      "domain": "authzed.com",
      "metadata": {
        "caveat_name": "somecaveat"
      }
    }
"""
ERROR_REASON_INVALID_SUBJECT_TYPE: ErrorReason.ValueType  # 10
"""The request tries to use a subject type that was not valid for a relation.

Example of an ErrorInfo:

    {  
      "reason": "ERROR_REASON_INVALID_SUBJECT_TYPE",
      "domain": "authzed.com",
      "metadata": {
        "definition_name": "somedefinition",
        "relation_name": "somerelation",
        "subject_type": "user:*"
      }
    }
"""
ERROR_REASON_CAVEAT_PARAMETER_TYPE_ERROR: ErrorReason.ValueType  # 11
"""The request tries to specify a caveat parameter value with the wrong type.

Example of an ErrorInfo:

    {  
      "reason": "ERROR_REASON_CAVEAT_PARAMETER_TYPE_ERROR",
      "domain": "authzed.com",
      "metadata": {
        "definition_name": "somedefinition",
        "relation_name": "somerelation",
        "caveat_name": "somecaveat",
        "parameter_name": "someparameter",
        "expected_type": "int",
      }
    }
"""
ERROR_REASON_UPDATES_ON_SAME_RELATIONSHIP: ErrorReason.ValueType  # 12
"""The request tries to perform two or more updates on the same relationship in the same WriteRelationships call.

Example of an ErrorInfo:

    {  
      "reason": "ERROR_REASON_UPDATES_ON_SAME_RELATIONSHIP",
      "domain": "authzed.com",
      "metadata": {
        "definition_name": "somedefinition",
        "relationship": "somerelationship",
      }
    }
"""
ERROR_REASON_CANNOT_UPDATE_PERMISSION: ErrorReason.ValueType  # 13
"""The request tries to write a relationship on a permission instead of a relation.

Example of an ErrorInfo:

    {  
      "reason": "ERROR_REASON_CANNOT_UPDATE_PERMISSION",
      "domain": "authzed.com",
      "metadata": {
        "definition_name": "somedefinition",
        "permission_name": "somerelation",
      }
    }
"""
ERROR_REASON_CAVEAT_EVALUATION_ERROR: ErrorReason.ValueType  # 14
"""The request failed to evaluate a caveat expression due to an error.

Example of an ErrorInfo:

    {  
      "reason": "ERROR_REASON_CAVEAT_EVALUATION_ERROR",
      "domain": "authzed.com",
      "metadata": {
        "caveat_name": "somecaveat",
      }
    }
"""
ERROR_REASON_INVALID_CURSOR: ErrorReason.ValueType  # 15
"""The request failed because the provided cursor was invalid in some way.

Example of an ErrorInfo:

    {  
      "reason": "ERROR_REASON_INVALID_CURSOR",
      "domain": "authzed.com",
      "metadata": {
         ... additional keys based on the kind of cursor error ...
      }
    }
"""
ERROR_REASON_TOO_MANY_RELATIONSHIPS_FOR_TRANSACTIONAL_DELETE: ErrorReason.ValueType  # 16
"""The request failed because there are too many matching relationships to be
deleted within a single transactional deletion call. To avoid, set
`optional_allow_partial_deletions` to true on the DeleteRelationships call.

Example of an ErrorInfo:

    {  
      "reason": "ERROR_REASON_TOO_MANY_RELATIONSHIPS_FOR_TRANSACTIONAL_DELETE",
      "domain": "authzed.com",
      "metadata": {
         ... fields for the filter ...
      }
    }
"""
ERROR_REASON_MAX_RELATIONSHIP_CONTEXT_SIZE: ErrorReason.ValueType  # 17
"""The request failed because the client attempted to write a relationship
with a context that exceeded the configured server limit.

Example of an ErrorInfo:

    {
      "reason": "ERROR_REASON_MAX_RELATIONSHIP_CONTEXT_SIZE",
      "domain": "authzed.com",
      "metadata": {
        "relationship":     "relationship_exceeding_the_limit",
        "max_allowed_size": "server_max_allowed_context_size",
        "context_size":     "actual_relationship_context_size" ,
      }
    }
"""
ERROR_REASON_ATTEMPT_TO_RECREATE_RELATIONSHIP: ErrorReason.ValueType  # 18
"""The request failed because a relationship marked to be CREATEd
was already present within the datastore.

Example of an ErrorInfo:

    {
      "reason": "ERROR_REASON_ATTEMPT_TO_RECREATE_RELATIONSHIP",
      "domain": "authzed.com",
      "metadata": {
        "relationship":          "relationship_that_already_existed",
        "resource_type":         "resource type",
        "resource_object_id":    "resource object id",
        ... additional decomposed relationship fields ...
      }
    }
"""
global___ErrorReason = ErrorReason
