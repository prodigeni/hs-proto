# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bnet/protocol/server_pool.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from .. import protocol_0_pb2 as bnet_dot_protocol__0__pb2
from . import attribute_pb2 as bnet_dot_protocol_dot_attribute__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='bnet/protocol/server_pool.proto',
  package='bnet.protocol.server_pool',
  syntax='proto2',
  serialized_pb=_b('\n\x1f\x62net/protocol/server_pool.proto\x12\x19\x62net.protocol.server_pool\x1a\x15\x62net/protocol_0.proto\x1a\x1d\x62net/protocol/attribute.proto\"\x10\n\x0eGetLoadRequest\"\x12\n\x10PoolStateRequest\"P\n\x0bServerState\x12\x17\n\x0c\x63urrent_load\x18\x01 \x01(\x02:\x01\x31\x12\x12\n\ngame_count\x18\x02 \x01(\r\x12\x14\n\x0cplayer_count\x18\x03 \x01(\r\"\xc7\x01\n\nServerInfo\x12&\n\x04host\x18\x01 \x01(\x0b\x32\x18.bnet.protocol.ProcessId\x12\x0f\n\x07replace\x18\x02 \x01(\x08\x12\x35\n\x05state\x18\x03 \x01(\x0b\x32&.bnet.protocol.server_pool.ServerState\x12\x35\n\tattribute\x18\x04 \x03(\x0b\x32\".bnet.protocol.attribute.Attribute\x12\x12\n\nprogram_id\x18\x05 \x01(\x07\"H\n\x11PoolStateResponse\x12\x33\n\x04info\x18\x01 \x03(\x0b\x32%.bnet.protocol.server_pool.ServerInfo')
  ,
  dependencies=[bnet_dot_protocol__0__pb2.DESCRIPTOR,bnet_dot_protocol_dot_attribute__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_GETLOADREQUEST = _descriptor.Descriptor(
  name='GetLoadRequest',
  full_name='bnet.protocol.server_pool.GetLoadRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=116,
  serialized_end=132,
)


_POOLSTATEREQUEST = _descriptor.Descriptor(
  name='PoolStateRequest',
  full_name='bnet.protocol.server_pool.PoolStateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=134,
  serialized_end=152,
)


_SERVERSTATE = _descriptor.Descriptor(
  name='ServerState',
  full_name='bnet.protocol.server_pool.ServerState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='current_load', full_name='bnet.protocol.server_pool.ServerState.current_load', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='game_count', full_name='bnet.protocol.server_pool.ServerState.game_count', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_count', full_name='bnet.protocol.server_pool.ServerState.player_count', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=154,
  serialized_end=234,
)


_SERVERINFO = _descriptor.Descriptor(
  name='ServerInfo',
  full_name='bnet.protocol.server_pool.ServerInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='host', full_name='bnet.protocol.server_pool.ServerInfo.host', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='replace', full_name='bnet.protocol.server_pool.ServerInfo.replace', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='state', full_name='bnet.protocol.server_pool.ServerInfo.state', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attribute', full_name='bnet.protocol.server_pool.ServerInfo.attribute', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='program_id', full_name='bnet.protocol.server_pool.ServerInfo.program_id', index=4,
      number=5, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=237,
  serialized_end=436,
)


_POOLSTATERESPONSE = _descriptor.Descriptor(
  name='PoolStateResponse',
  full_name='bnet.protocol.server_pool.PoolStateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='info', full_name='bnet.protocol.server_pool.PoolStateResponse.info', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=438,
  serialized_end=510,
)

_SERVERINFO.fields_by_name['host'].message_type = bnet_dot_protocol__0__pb2._PROCESSID
_SERVERINFO.fields_by_name['state'].message_type = _SERVERSTATE
_SERVERINFO.fields_by_name['attribute'].message_type = bnet_dot_protocol_dot_attribute__pb2._ATTRIBUTE
_POOLSTATERESPONSE.fields_by_name['info'].message_type = _SERVERINFO
DESCRIPTOR.message_types_by_name['GetLoadRequest'] = _GETLOADREQUEST
DESCRIPTOR.message_types_by_name['PoolStateRequest'] = _POOLSTATEREQUEST
DESCRIPTOR.message_types_by_name['ServerState'] = _SERVERSTATE
DESCRIPTOR.message_types_by_name['ServerInfo'] = _SERVERINFO
DESCRIPTOR.message_types_by_name['PoolStateResponse'] = _POOLSTATERESPONSE

GetLoadRequest = _reflection.GeneratedProtocolMessageType('GetLoadRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETLOADREQUEST,
  __module__ = 'bnet.protocol.server_pool_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.server_pool.GetLoadRequest)
  ))
_sym_db.RegisterMessage(GetLoadRequest)

PoolStateRequest = _reflection.GeneratedProtocolMessageType('PoolStateRequest', (_message.Message,), dict(
  DESCRIPTOR = _POOLSTATEREQUEST,
  __module__ = 'bnet.protocol.server_pool_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.server_pool.PoolStateRequest)
  ))
_sym_db.RegisterMessage(PoolStateRequest)

ServerState = _reflection.GeneratedProtocolMessageType('ServerState', (_message.Message,), dict(
  DESCRIPTOR = _SERVERSTATE,
  __module__ = 'bnet.protocol.server_pool_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.server_pool.ServerState)
  ))
_sym_db.RegisterMessage(ServerState)

ServerInfo = _reflection.GeneratedProtocolMessageType('ServerInfo', (_message.Message,), dict(
  DESCRIPTOR = _SERVERINFO,
  __module__ = 'bnet.protocol.server_pool_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.server_pool.ServerInfo)
  ))
_sym_db.RegisterMessage(ServerInfo)

PoolStateResponse = _reflection.GeneratedProtocolMessageType('PoolStateResponse', (_message.Message,), dict(
  DESCRIPTOR = _POOLSTATERESPONSE,
  __module__ = 'bnet.protocol.server_pool_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.server_pool.PoolStateResponse)
  ))
_sym_db.RegisterMessage(PoolStateResponse)


# @@protoc_insertion_point(module_scope)
