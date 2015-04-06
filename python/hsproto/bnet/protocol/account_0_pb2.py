# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bnet/protocol/account_0.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='bnet/protocol/account_0.proto',
  package='bnet.protocol.account',
  syntax='proto2',
  serialized_pb=_b('\n\x1d\x62net/protocol/account_0.proto\x12\x15\x62net.protocol.account\"-\n\x11\x41\x63\x63ountCredential\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"\xe3\x01\n\x13\x41\x63\x63ountFieldOptions\x12\x12\n\nall_fields\x18\x01 \x01(\x08\x12 \n\x18\x66ield_account_level_info\x18\x02 \x01(\x08\x12\x1a\n\x12\x66ield_privacy_info\x18\x03 \x01(\x08\x12#\n\x1b\x66ield_parental_control_info\x18\x04 \x01(\x08\x12\x1d\n\x15\x66ield_game_level_info\x18\x06 \x01(\x08\x12\x19\n\x11\x66ield_game_status\x18\x07 \x01(\x08\x12\x1b\n\x13\x66ield_game_accounts\x18\x08 \x01(\x08\"\x17\n\tAccountId\x12\n\n\x02id\x18\x01 \x01(\x07\"-\n\x0e\x41\x63\x63ountLicense\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0f\n\x07\x65xpires\x18\x02 \x01(\x04')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ACCOUNTCREDENTIAL = _descriptor.Descriptor(
  name='AccountCredential',
  full_name='bnet.protocol.account.AccountCredential',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='bnet.protocol.account.AccountCredential.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='bnet.protocol.account.AccountCredential.data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=56,
  serialized_end=101,
)


_ACCOUNTFIELDOPTIONS = _descriptor.Descriptor(
  name='AccountFieldOptions',
  full_name='bnet.protocol.account.AccountFieldOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='all_fields', full_name='bnet.protocol.account.AccountFieldOptions.all_fields', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='field_account_level_info', full_name='bnet.protocol.account.AccountFieldOptions.field_account_level_info', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='field_privacy_info', full_name='bnet.protocol.account.AccountFieldOptions.field_privacy_info', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='field_parental_control_info', full_name='bnet.protocol.account.AccountFieldOptions.field_parental_control_info', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='field_game_level_info', full_name='bnet.protocol.account.AccountFieldOptions.field_game_level_info', index=4,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='field_game_status', full_name='bnet.protocol.account.AccountFieldOptions.field_game_status', index=5,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='field_game_accounts', full_name='bnet.protocol.account.AccountFieldOptions.field_game_accounts', index=6,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=104,
  serialized_end=331,
)


_ACCOUNTID = _descriptor.Descriptor(
  name='AccountId',
  full_name='bnet.protocol.account.AccountId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='bnet.protocol.account.AccountId.id', index=0,
      number=1, type=7, cpp_type=3, label=1,
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
  serialized_start=333,
  serialized_end=356,
)


_ACCOUNTLICENSE = _descriptor.Descriptor(
  name='AccountLicense',
  full_name='bnet.protocol.account.AccountLicense',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='bnet.protocol.account.AccountLicense.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='expires', full_name='bnet.protocol.account.AccountLicense.expires', index=1,
      number=2, type=4, cpp_type=4, label=1,
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
  serialized_start=358,
  serialized_end=403,
)

DESCRIPTOR.message_types_by_name['AccountCredential'] = _ACCOUNTCREDENTIAL
DESCRIPTOR.message_types_by_name['AccountFieldOptions'] = _ACCOUNTFIELDOPTIONS
DESCRIPTOR.message_types_by_name['AccountId'] = _ACCOUNTID
DESCRIPTOR.message_types_by_name['AccountLicense'] = _ACCOUNTLICENSE

AccountCredential = _reflection.GeneratedProtocolMessageType('AccountCredential', (_message.Message,), dict(
  DESCRIPTOR = _ACCOUNTCREDENTIAL,
  __module__ = 'bnet.protocol.account_0_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.account.AccountCredential)
  ))
_sym_db.RegisterMessage(AccountCredential)

AccountFieldOptions = _reflection.GeneratedProtocolMessageType('AccountFieldOptions', (_message.Message,), dict(
  DESCRIPTOR = _ACCOUNTFIELDOPTIONS,
  __module__ = 'bnet.protocol.account_0_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.account.AccountFieldOptions)
  ))
_sym_db.RegisterMessage(AccountFieldOptions)

AccountId = _reflection.GeneratedProtocolMessageType('AccountId', (_message.Message,), dict(
  DESCRIPTOR = _ACCOUNTID,
  __module__ = 'bnet.protocol.account_0_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.account.AccountId)
  ))
_sym_db.RegisterMessage(AccountId)

AccountLicense = _reflection.GeneratedProtocolMessageType('AccountLicense', (_message.Message,), dict(
  DESCRIPTOR = _ACCOUNTLICENSE,
  __module__ = 'bnet.protocol.account_0_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.account.AccountLicense)
  ))
_sym_db.RegisterMessage(AccountLicense)


# @@protoc_insertion_point(module_scope)
