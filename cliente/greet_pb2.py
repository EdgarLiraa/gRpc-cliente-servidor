# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: greet.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bgreet.proto\x12\x05greet\"\r\n\x0bVoidRequest\"\x0b\n\tVoidReply\"\x1c\n\x0bLongRequest\x12\r\n\x05value\x18\x01 \x01(\x03\"\x1b\n\tLongReply\x12\x0e\n\x06result\x18\x01 \x01(\x03\"\x84\x01\n\x12LongComplexRequest\x12\x0c\n\x04\x61rg1\x18\x01 \x01(\x03\x12\x0c\n\x04\x61rg2\x18\x02 \x01(\x03\x12\x0c\n\x04\x61rg3\x18\x03 \x01(\x03\x12\x0c\n\x04\x61rg4\x18\x04 \x01(\x03\x12\x0c\n\x04\x61rg5\x18\x05 \x01(\x03\x12\x0c\n\x04\x61rg6\x18\x06 \x01(\x03\x12\x0c\n\x04\x61rg7\x18\x07 \x01(\x03\x12\x0c\n\x04\x61rg8\x18\x08 \x01(\x03\"\"\n\x10LongComplexReply\x12\x0e\n\x06result\x18\x01 \x01(\x03\"\x1d\n\rStringRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1e\n\x0bStringReply\x12\x0f\n\x07message\x18\x01 \x01(\t\"5\n\x06Pessoa\x12\x0c\n\x04nome\x18\x01 \x01(\t\x12\r\n\x05idade\x18\x02 \x01(\x05\x12\x0e\n\x06\x61ltura\x18\x03 \x01(\x02\"\x1b\n\rClasseRequest\x12\n\n\x02id\x18\x01 \x01(\x05\",\n\x0b\x43lasseReply\x12\x1d\n\x06person\x18\x01 \x01(\x0b\x32\r.greet.Pessoa2\xb0\x02\n\x07Greeter\x12\x31\n\tVoidTeste\x12\x12.greet.VoidRequest\x1a\x10.greet.VoidReply\x12\x38\n\x10LongSimplesTeste\x12\x12.greet.LongRequest\x1a\x10.greet.LongReply\x12G\n\x11LongComplexoTeste\x12\x19.greet.LongComplexRequest\x1a\x17.greet.LongComplexReply\x12\x37\n\x0bStringTeste\x12\x14.greet.StringRequest\x1a\x12.greet.StringReply\x12\x36\n\nClassTeste\x12\x14.greet.ClasseRequest\x1a\x12.greet.ClasseReplyb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'greet_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _VOIDREQUEST._serialized_start=22
  _VOIDREQUEST._serialized_end=35
  _VOIDREPLY._serialized_start=37
  _VOIDREPLY._serialized_end=48
  _LONGREQUEST._serialized_start=50
  _LONGREQUEST._serialized_end=78
  _LONGREPLY._serialized_start=80
  _LONGREPLY._serialized_end=107
  _LONGCOMPLEXREQUEST._serialized_start=110
  _LONGCOMPLEXREQUEST._serialized_end=242
  _LONGCOMPLEXREPLY._serialized_start=244
  _LONGCOMPLEXREPLY._serialized_end=278
  _STRINGREQUEST._serialized_start=280
  _STRINGREQUEST._serialized_end=309
  _STRINGREPLY._serialized_start=311
  _STRINGREPLY._serialized_end=341
  _PESSOA._serialized_start=343
  _PESSOA._serialized_end=396
  _CLASSEREQUEST._serialized_start=398
  _CLASSEREQUEST._serialized_end=425
  _CLASSEREPLY._serialized_start=427
  _CLASSEREPLY._serialized_end=471
  _GREETER._serialized_start=474
  _GREETER._serialized_end=778
# @@protoc_insertion_point(module_scope)
