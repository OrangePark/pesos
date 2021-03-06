# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: state.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='state.proto',
  package='mesos.internal.state',
  serialized_pb='\n\x0bstate.proto\x12\x14mesos.internal.state\"2\n\x05\x45ntry\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x0c\n\x04uuid\x18\x02 \x02(\x0c\x12\r\n\x05value\x18\x03 \x02(\x0c\"\xa9\x02\n\tOperation\x12\x32\n\x04type\x18\x01 \x02(\x0e\x32$.mesos.internal.state.Operation.Type\x12:\n\x08snapshot\x18\x02 \x01(\x0b\x32(.mesos.internal.state.Operation.Snapshot\x12\x38\n\x07\x65xpunge\x18\x03 \x01(\x0b\x32\'.mesos.internal.state.Operation.Expunge\x1a\x36\n\x08Snapshot\x12*\n\x05\x65ntry\x18\x01 \x02(\x0b\x32\x1b.mesos.internal.state.Entry\x1a\x17\n\x07\x45xpunge\x12\x0c\n\x04name\x18\x01 \x02(\t\"!\n\x04Type\x12\x0c\n\x08SNAPSHOT\x10\x01\x12\x0b\n\x07\x45XPUNGE\x10\x02')



_OPERATION_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='mesos.internal.state.Operation.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SNAPSHOT', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXPUNGE', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=354,
  serialized_end=387,
)


_ENTRY = _descriptor.Descriptor(
  name='Entry',
  full_name='mesos.internal.state.Entry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='mesos.internal.state.Entry.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uuid', full_name='mesos.internal.state.Entry.uuid', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='mesos.internal.state.Entry.value', index=2,
      number=3, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
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
  extension_ranges=[],
  serialized_start=37,
  serialized_end=87,
)


_OPERATION_SNAPSHOT = _descriptor.Descriptor(
  name='Snapshot',
  full_name='mesos.internal.state.Operation.Snapshot',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entry', full_name='mesos.internal.state.Operation.Snapshot.entry', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
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
  extension_ranges=[],
  serialized_start=273,
  serialized_end=327,
)

_OPERATION_EXPUNGE = _descriptor.Descriptor(
  name='Expunge',
  full_name='mesos.internal.state.Operation.Expunge',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='mesos.internal.state.Operation.Expunge.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  extension_ranges=[],
  serialized_start=329,
  serialized_end=352,
)

_OPERATION = _descriptor.Descriptor(
  name='Operation',
  full_name='mesos.internal.state.Operation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='mesos.internal.state.Operation.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='snapshot', full_name='mesos.internal.state.Operation.snapshot', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='expunge', full_name='mesos.internal.state.Operation.expunge', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_OPERATION_SNAPSHOT, _OPERATION_EXPUNGE, ],
  enum_types=[
    _OPERATION_TYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=90,
  serialized_end=387,
)

_OPERATION_SNAPSHOT.fields_by_name['entry'].message_type = _ENTRY
_OPERATION_SNAPSHOT.containing_type = _OPERATION;
_OPERATION_EXPUNGE.containing_type = _OPERATION;
_OPERATION.fields_by_name['type'].enum_type = _OPERATION_TYPE
_OPERATION.fields_by_name['snapshot'].message_type = _OPERATION_SNAPSHOT
_OPERATION.fields_by_name['expunge'].message_type = _OPERATION_EXPUNGE
_OPERATION_TYPE.containing_type = _OPERATION;
DESCRIPTOR.message_types_by_name['Entry'] = _ENTRY
DESCRIPTOR.message_types_by_name['Operation'] = _OPERATION

class Entry(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ENTRY

  # @@protoc_insertion_point(class_scope:mesos.internal.state.Entry)

class Operation(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType

  class Snapshot(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _OPERATION_SNAPSHOT

    # @@protoc_insertion_point(class_scope:mesos.internal.state.Operation.Snapshot)

  class Expunge(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _OPERATION_EXPUNGE

    # @@protoc_insertion_point(class_scope:mesos.internal.state.Operation.Expunge)
  DESCRIPTOR = _OPERATION

  # @@protoc_insertion_point(class_scope:mesos.internal.state.Operation)


# @@protoc_insertion_point(module_scope)
