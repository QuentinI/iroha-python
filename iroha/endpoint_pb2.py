# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: endpoint.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import transaction_pb2 as transaction__pb2
from . import queries_pb2 as queries__pb2
from . import qry_responses_pb2 as qry__responses__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='endpoint.proto',
  package='iroha.protocol',
  syntax='proto3',
  serialized_options=b'Z\030iroha.generated/protocol',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0e\x65ndpoint.proto\x12\x0eiroha.protocol\x1a\x11transaction.proto\x1a\rqueries.proto\x1a\x13qry_responses.proto\x1a\x1bgoogle/protobuf/empty.proto\"\x94\x01\n\rToriiResponse\x12+\n\ttx_status\x18\x01 \x01(\x0e\x32\x18.iroha.protocol.TxStatus\x12\x0f\n\x07tx_hash\x18\x02 \x01(\t\x12\x17\n\x0f\x65rr_or_cmd_name\x18\x03 \x01(\t\x12\x18\n\x10\x66\x61iled_cmd_index\x18\x04 \x01(\x04\x12\x12\n\nerror_code\x18\x05 \x01(\r\"\"\n\x0fTxStatusRequest\x12\x0f\n\x07tx_hash\x18\x01 \x01(\t\";\n\x06TxList\x12\x31\n\x0ctransactions\x18\x01 \x03(\x0b\x32\x1b.iroha.protocol.Transaction*\x80\x02\n\x08TxStatus\x12\x1f\n\x1bSTATELESS_VALIDATION_FAILED\x10\x00\x12 \n\x1cSTATELESS_VALIDATION_SUCCESS\x10\x01\x12\x1e\n\x1aSTATEFUL_VALIDATION_FAILED\x10\x02\x12\x1f\n\x1bSTATEFUL_VALIDATION_SUCCESS\x10\x03\x12\x0c\n\x08REJECTED\x10\x04\x12\r\n\tCOMMITTED\x10\x05\x12\x0f\n\x0bMST_EXPIRED\x10\x06\x12\x10\n\x0cNOT_RECEIVED\x10\x07\x12\x0f\n\x0bMST_PENDING\x10\x08\x12\x1f\n\x1b\x45NOUGH_SIGNATURES_COLLECTED\x10\t2\xaa\x02\n\x11\x43ommandService_v1\x12<\n\x05Torii\x12\x1b.iroha.protocol.Transaction\x1a\x16.google.protobuf.Empty\x12;\n\tListTorii\x12\x16.iroha.protocol.TxList\x1a\x16.google.protobuf.Empty\x12H\n\x06Status\x12\x1f.iroha.protocol.TxStatusRequest\x1a\x1d.iroha.protocol.ToriiResponse\x12P\n\x0cStatusStream\x12\x1f.iroha.protocol.TxStatusRequest\x1a\x1d.iroha.protocol.ToriiResponse0\x01\x32\xea\x01\n\x0fQueryService_v1\x12<\n\x04\x46ind\x12\x15.iroha.protocol.Query\x1a\x1d.iroha.protocol.QueryResponse\x12Q\n\x0c\x46\x65tchCommits\x12\x1b.iroha.protocol.BlocksQuery\x1a\".iroha.protocol.BlockQueryResponse0\x01\x12\x46\n\x0bHealthcheck\x12\x16.google.protobuf.Empty\x1a\x1f.iroha.protocol.HealthcheckDataB\x1aZ\x18iroha.generated/protocolb\x06proto3'
  ,
  dependencies=[transaction__pb2.DESCRIPTOR,queries__pb2.DESCRIPTOR,qry__responses__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])

_TXSTATUS = _descriptor.EnumDescriptor(
  name='TxStatus',
  full_name='iroha.protocol.TxStatus',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATELESS_VALIDATION_FAILED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STATELESS_VALIDATION_SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STATEFUL_VALIDATION_FAILED', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STATEFUL_VALIDATION_SUCCESS', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='REJECTED', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='COMMITTED', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MST_EXPIRED', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NOT_RECEIVED', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MST_PENDING', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ENOUGH_SIGNATURES_COLLECTED', index=9, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=367,
  serialized_end=623,
)
_sym_db.RegisterEnumDescriptor(_TXSTATUS)

TxStatus = enum_type_wrapper.EnumTypeWrapper(_TXSTATUS)
STATELESS_VALIDATION_FAILED = 0
STATELESS_VALIDATION_SUCCESS = 1
STATEFUL_VALIDATION_FAILED = 2
STATEFUL_VALIDATION_SUCCESS = 3
REJECTED = 4
COMMITTED = 5
MST_EXPIRED = 6
NOT_RECEIVED = 7
MST_PENDING = 8
ENOUGH_SIGNATURES_COLLECTED = 9



_TORIIRESPONSE = _descriptor.Descriptor(
  name='ToriiResponse',
  full_name='iroha.protocol.ToriiResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tx_status', full_name='iroha.protocol.ToriiResponse.tx_status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tx_hash', full_name='iroha.protocol.ToriiResponse.tx_hash', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='err_or_cmd_name', full_name='iroha.protocol.ToriiResponse.err_or_cmd_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='failed_cmd_index', full_name='iroha.protocol.ToriiResponse.failed_cmd_index', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error_code', full_name='iroha.protocol.ToriiResponse.error_code', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=119,
  serialized_end=267,
)


_TXSTATUSREQUEST = _descriptor.Descriptor(
  name='TxStatusRequest',
  full_name='iroha.protocol.TxStatusRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tx_hash', full_name='iroha.protocol.TxStatusRequest.tx_hash', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=269,
  serialized_end=303,
)


_TXLIST = _descriptor.Descriptor(
  name='TxList',
  full_name='iroha.protocol.TxList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='transactions', full_name='iroha.protocol.TxList.transactions', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=305,
  serialized_end=364,
)

_TORIIRESPONSE.fields_by_name['tx_status'].enum_type = _TXSTATUS
_TXLIST.fields_by_name['transactions'].message_type = transaction__pb2._TRANSACTION
DESCRIPTOR.message_types_by_name['ToriiResponse'] = _TORIIRESPONSE
DESCRIPTOR.message_types_by_name['TxStatusRequest'] = _TXSTATUSREQUEST
DESCRIPTOR.message_types_by_name['TxList'] = _TXLIST
DESCRIPTOR.enum_types_by_name['TxStatus'] = _TXSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ToriiResponse = _reflection.GeneratedProtocolMessageType('ToriiResponse', (_message.Message,), {
  'DESCRIPTOR' : _TORIIRESPONSE,
  '__module__' : 'endpoint_pb2'
  # @@protoc_insertion_point(class_scope:iroha.protocol.ToriiResponse)
  })
_sym_db.RegisterMessage(ToriiResponse)

TxStatusRequest = _reflection.GeneratedProtocolMessageType('TxStatusRequest', (_message.Message,), {
  'DESCRIPTOR' : _TXSTATUSREQUEST,
  '__module__' : 'endpoint_pb2'
  # @@protoc_insertion_point(class_scope:iroha.protocol.TxStatusRequest)
  })
_sym_db.RegisterMessage(TxStatusRequest)

TxList = _reflection.GeneratedProtocolMessageType('TxList', (_message.Message,), {
  'DESCRIPTOR' : _TXLIST,
  '__module__' : 'endpoint_pb2'
  # @@protoc_insertion_point(class_scope:iroha.protocol.TxList)
  })
_sym_db.RegisterMessage(TxList)


DESCRIPTOR._options = None

_COMMANDSERVICE_V1 = _descriptor.ServiceDescriptor(
  name='CommandService_v1',
  full_name='iroha.protocol.CommandService_v1',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=626,
  serialized_end=924,
  methods=[
  _descriptor.MethodDescriptor(
    name='Torii',
    full_name='iroha.protocol.CommandService_v1.Torii',
    index=0,
    containing_service=None,
    input_type=transaction__pb2._TRANSACTION,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ListTorii',
    full_name='iroha.protocol.CommandService_v1.ListTorii',
    index=1,
    containing_service=None,
    input_type=_TXLIST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Status',
    full_name='iroha.protocol.CommandService_v1.Status',
    index=2,
    containing_service=None,
    input_type=_TXSTATUSREQUEST,
    output_type=_TORIIRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='StatusStream',
    full_name='iroha.protocol.CommandService_v1.StatusStream',
    index=3,
    containing_service=None,
    input_type=_TXSTATUSREQUEST,
    output_type=_TORIIRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_COMMANDSERVICE_V1)

DESCRIPTOR.services_by_name['CommandService_v1'] = _COMMANDSERVICE_V1


_QUERYSERVICE_V1 = _descriptor.ServiceDescriptor(
  name='QueryService_v1',
  full_name='iroha.protocol.QueryService_v1',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=927,
  serialized_end=1161,
  methods=[
  _descriptor.MethodDescriptor(
    name='Find',
    full_name='iroha.protocol.QueryService_v1.Find',
    index=0,
    containing_service=None,
    input_type=queries__pb2._QUERY,
    output_type=qry__responses__pb2._QUERYRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='FetchCommits',
    full_name='iroha.protocol.QueryService_v1.FetchCommits',
    index=1,
    containing_service=None,
    input_type=queries__pb2._BLOCKSQUERY,
    output_type=qry__responses__pb2._BLOCKQUERYRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Healthcheck',
    full_name='iroha.protocol.QueryService_v1.Healthcheck',
    index=2,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=qry__responses__pb2._HEALTHCHECKDATA,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_QUERYSERVICE_V1)

DESCRIPTOR.services_by_name['QueryService_v1'] = _QUERYSERVICE_V1

# @@protoc_insertion_point(module_scope)
