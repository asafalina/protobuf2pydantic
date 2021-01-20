# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ssss.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ssss.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\nssss.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xf2\x02\n\x07Payload\x12\t\n\x01\x61\x18\x01 \x01(\x05\x12\t\n\x01\x62\x18\x02 \x01(\t\x12\x1a\n\x01\x63\x18\x03 \x03(\x0b\x32\x0f.Payload.CEntry\x12\x17\n\x01\x64\x18\x04 \x01(\x0b\x32\x0c.Payload.wow\x12\x1a\n\x01\x65\x18\x05 \x03(\x0b\x32\x0f.Payload.EEntry\x12\"\n\x01\x66\x18\x06 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x18\n\x01g\x18\x07 \x03(\x0b\x32\r.Payload.wows\x12\"\n\x01h\x18\x08 \x03(\x0b\x32\x17.google.protobuf.Struct\x12%\n\x01i\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x1a(\n\x06\x43\x45ntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a\x10\n\x03wow\x12\t\n\x01z\x18\x01 \x01(\t\x1a(\n\x06\x45\x45ntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x11\n\x04wows\x12\t\n\x01z\x18\x01 \x01(\t\" \n\x08Response\x12\t\n\x01\x61\x18\x01 \x01(\x05\x12\t\n\x01\x62\x18\x02 \x01(\t2F\n\x04Test\x12\x1e\n\x03One\x12\x08.Payload\x1a\t.Response\"\x00(\x01\x12\x1e\n\x03Two\x12\x08.Payload\x1a\t.Response\"\x00(\x01\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_PAYLOAD_CENTRY = _descriptor.Descriptor(
  name='CEntry',
  full_name='Payload.CEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='Payload.CEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='Payload.CEntry.value', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=329,
  serialized_end=369,
)

_PAYLOAD_WOW = _descriptor.Descriptor(
  name='wow',
  full_name='Payload.wow',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='z', full_name='Payload.wow.z', index=0,
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
  serialized_start=371,
  serialized_end=387,
)

_PAYLOAD_EENTRY = _descriptor.Descriptor(
  name='EEntry',
  full_name='Payload.EEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='Payload.EEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='Payload.EEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=389,
  serialized_end=429,
)

_PAYLOAD_WOWS = _descriptor.Descriptor(
  name='wows',
  full_name='Payload.wows',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='z', full_name='Payload.wows.z', index=0,
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
  serialized_start=431,
  serialized_end=448,
)

_PAYLOAD = _descriptor.Descriptor(
  name='Payload',
  full_name='Payload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='a', full_name='Payload.a', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='b', full_name='Payload.b', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='c', full_name='Payload.c', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='d', full_name='Payload.d', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='e', full_name='Payload.e', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='f', full_name='Payload.f', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='g', full_name='Payload.g', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='h', full_name='Payload.h', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='i', full_name='Payload.i', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_PAYLOAD_CENTRY, _PAYLOAD_WOW, _PAYLOAD_EENTRY, _PAYLOAD_WOWS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=78,
  serialized_end=448,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='a', full_name='Response.a', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='b', full_name='Response.b', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=450,
  serialized_end=482,
)

_PAYLOAD_CENTRY.containing_type = _PAYLOAD
_PAYLOAD_WOW.containing_type = _PAYLOAD
_PAYLOAD_EENTRY.containing_type = _PAYLOAD
_PAYLOAD_WOWS.containing_type = _PAYLOAD
_PAYLOAD.fields_by_name['c'].message_type = _PAYLOAD_CENTRY
_PAYLOAD.fields_by_name['d'].message_type = _PAYLOAD_WOW
_PAYLOAD.fields_by_name['e'].message_type = _PAYLOAD_EENTRY
_PAYLOAD.fields_by_name['f'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_PAYLOAD.fields_by_name['g'].message_type = _PAYLOAD_WOWS
_PAYLOAD.fields_by_name['h'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_PAYLOAD.fields_by_name['i'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['Payload'] = _PAYLOAD
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Payload = _reflection.GeneratedProtocolMessageType('Payload', (_message.Message,), {

  'CEntry' : _reflection.GeneratedProtocolMessageType('CEntry', (_message.Message,), {
    'DESCRIPTOR' : _PAYLOAD_CENTRY,
    '__module__' : 'ssss_pb2'
    # @@protoc_insertion_point(class_scope:Payload.CEntry)
    })
  ,

  'wow' : _reflection.GeneratedProtocolMessageType('wow', (_message.Message,), {
    'DESCRIPTOR' : _PAYLOAD_WOW,
    '__module__' : 'ssss_pb2'
    # @@protoc_insertion_point(class_scope:Payload.wow)
    })
  ,

  'EEntry' : _reflection.GeneratedProtocolMessageType('EEntry', (_message.Message,), {
    'DESCRIPTOR' : _PAYLOAD_EENTRY,
    '__module__' : 'ssss_pb2'
    # @@protoc_insertion_point(class_scope:Payload.EEntry)
    })
  ,

  'wows' : _reflection.GeneratedProtocolMessageType('wows', (_message.Message,), {
    'DESCRIPTOR' : _PAYLOAD_WOWS,
    '__module__' : 'ssss_pb2'
    # @@protoc_insertion_point(class_scope:Payload.wows)
    })
  ,
  'DESCRIPTOR' : _PAYLOAD,
  '__module__' : 'ssss_pb2'
  # @@protoc_insertion_point(class_scope:Payload)
  })
_sym_db.RegisterMessage(Payload)
_sym_db.RegisterMessage(Payload.CEntry)
_sym_db.RegisterMessage(Payload.wow)
_sym_db.RegisterMessage(Payload.EEntry)
_sym_db.RegisterMessage(Payload.wows)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'ssss_pb2'
  # @@protoc_insertion_point(class_scope:Response)
  })
_sym_db.RegisterMessage(Response)


_PAYLOAD_CENTRY._options = None
_PAYLOAD_EENTRY._options = None

_TEST = _descriptor.ServiceDescriptor(
  name='Test',
  full_name='Test',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=484,
  serialized_end=554,
  methods=[
  _descriptor.MethodDescriptor(
    name='One',
    full_name='Test.One',
    index=0,
    containing_service=None,
    input_type=_PAYLOAD,
    output_type=_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Two',
    full_name='Test.Two',
    index=1,
    containing_service=None,
    input_type=_PAYLOAD,
    output_type=_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_TEST)

DESCRIPTOR.services_by_name['Test'] = _TEST

# @@protoc_insertion_point(module_scope)
