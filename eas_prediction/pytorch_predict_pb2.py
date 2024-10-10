# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pytorch_predict.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pytorch_predict.proto',
  package='pytorch.eas',
  syntax='proto3',
  serialized_options=_b('\370\001\001'),
  serialized_pb=_b('\n\x15pytorch_predict.proto\x12\x0bpytorch.eas\"\x1d\n\nArrayShape\x12\x0f\n\x03\x64im\x18\x01 \x03(\x03\x42\x02\x10\x01\"\xd4\x01\n\nArrayProto\x12)\n\x05\x64type\x18\x01 \x01(\x0e\x32\x1a.pytorch.eas.ArrayDataType\x12,\n\x0b\x61rray_shape\x18\x02 \x01(\x0b\x32\x17.pytorch.eas.ArrayShape\x12\x15\n\tfloat_val\x18\x03 \x03(\x02\x42\x02\x10\x01\x12\x16\n\ndouble_val\x18\x04 \x03(\x01\x42\x02\x10\x01\x12\x13\n\x07int_val\x18\x05 \x03(\x05\x42\x02\x10\x01\x12\x12\n\nstring_val\x18\x06 \x03(\x0c\x12\x15\n\tint64_val\x18\x07 \x03(\x03\x42\x02\x10\x01\"\xf0\x01\n\x0ePredictRequest\x12\'\n\x06inputs\x18\x01 \x03(\x0b\x32\x17.pytorch.eas.ArrayProto\x12\x15\n\routput_filter\x18\x02 \x03(\x05\x12>\n\nmap_inputs\x18\x03 \x03(\x0b\x32*.pytorch.eas.PredictRequest.MapInputsEntry\x12\x13\n\x0b\x64\x65\x62ug_level\x18\x64 \x01(\x05\x1aI\n\x0eMapInputsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12&\n\x05value\x18\x02 \x01(\x0b\x32\x17.pytorch.eas.ArrayProto:\x02\x38\x01\"\xca\x01\n\x0fPredictResponse\x12(\n\x07outputs\x18\x01 \x03(\x0b\x32\x17.pytorch.eas.ArrayProto\x12\x41\n\x0bmap_outputs\x18\x02 \x03(\x0b\x32,.pytorch.eas.PredictResponse.MapOutputsEntry\x1aJ\n\x0fMapOutputsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12&\n\x05value\x18\x02 \x01(\x0b\x32\x17.pytorch.eas.ArrayProto:\x02\x38\x01*\xdb\x02\n\rArrayDataType\x12\x0e\n\nDT_INVALID\x10\x00\x12\x0c\n\x08\x44T_FLOAT\x10\x01\x12\r\n\tDT_DOUBLE\x10\x02\x12\x0c\n\x08\x44T_INT32\x10\x03\x12\x0c\n\x08\x44T_UINT8\x10\x04\x12\x0c\n\x08\x44T_INT16\x10\x05\x12\x0b\n\x07\x44T_INT8\x10\x06\x12\r\n\tDT_STRING\x10\x07\x12\x10\n\x0c\x44T_COMPLEX64\x10\x08\x12\x0c\n\x08\x44T_INT64\x10\t\x12\x0b\n\x07\x44T_BOOL\x10\n\x12\x0c\n\x08\x44T_QINT8\x10\x0b\x12\r\n\tDT_QUINT8\x10\x0c\x12\r\n\tDT_QINT32\x10\r\x12\x0f\n\x0b\x44T_BFLOAT16\x10\x0e\x12\r\n\tDT_QINT16\x10\x0f\x12\x0e\n\nDT_QUINT16\x10\x10\x12\r\n\tDT_UINT16\x10\x11\x12\x11\n\rDT_COMPLEX128\x10\x12\x12\x0b\n\x07\x44T_HALF\x10\x13\x12\x0f\n\x0b\x44T_RESOURCE\x10\x14\x12\x0e\n\nDT_VARIANT\x10\x15\x42\x03\xf8\x01\x01\x62\x06proto3')
)

_ARRAYDATATYPE = _descriptor.EnumDescriptor(
  name='ArrayDataType',
  full_name='pytorch.eas.ArrayDataType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DT_INVALID', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DT_FLOAT', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DT_DOUBLE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DT_INT32', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DT_UINT8', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DT_INT16', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DT_INT8', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DT_STRING', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DT_COMPLEX64', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DT_INT64', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DT_BOOL', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DT_QINT8', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DT_QUINT8', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DT_QINT32', index=13, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DT_BFLOAT16', index=14, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DT_QINT16', index=15, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DT_QUINT16', index=16, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DT_UINT16', index=17, number=17,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DT_COMPLEX128', index=18, number=18,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DT_HALF', index=19, number=19,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DT_RESOURCE', index=20, number=20,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DT_VARIANT', index=21, number=21,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=733,
  serialized_end=1080,
)
_sym_db.RegisterEnumDescriptor(_ARRAYDATATYPE)

ArrayDataType = enum_type_wrapper.EnumTypeWrapper(_ARRAYDATATYPE)
DT_INVALID = 0
DT_FLOAT = 1
DT_DOUBLE = 2
DT_INT32 = 3
DT_UINT8 = 4
DT_INT16 = 5
DT_INT8 = 6
DT_STRING = 7
DT_COMPLEX64 = 8
DT_INT64 = 9
DT_BOOL = 10
DT_QINT8 = 11
DT_QUINT8 = 12
DT_QINT32 = 13
DT_BFLOAT16 = 14
DT_QINT16 = 15
DT_QUINT16 = 16
DT_UINT16 = 17
DT_COMPLEX128 = 18
DT_HALF = 19
DT_RESOURCE = 20
DT_VARIANT = 21



_ARRAYSHAPE = _descriptor.Descriptor(
  name='ArrayShape',
  full_name='pytorch.eas.ArrayShape',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dim', full_name='pytorch.eas.ArrayShape.dim', index=0,
      number=1, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
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
  serialized_start=38,
  serialized_end=67,
)


_ARRAYPROTO = _descriptor.Descriptor(
  name='ArrayProto',
  full_name='pytorch.eas.ArrayProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dtype', full_name='pytorch.eas.ArrayProto.dtype', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='array_shape', full_name='pytorch.eas.ArrayProto.array_shape', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='float_val', full_name='pytorch.eas.ArrayProto.float_val', index=2,
      number=3, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='double_val', full_name='pytorch.eas.ArrayProto.double_val', index=3,
      number=4, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='int_val', full_name='pytorch.eas.ArrayProto.int_val', index=4,
      number=5, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='string_val', full_name='pytorch.eas.ArrayProto.string_val', index=5,
      number=6, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='int64_val', full_name='pytorch.eas.ArrayProto.int64_val', index=6,
      number=7, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
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
  serialized_start=70,
  serialized_end=282,
)


_PREDICTREQUEST_MAPINPUTSENTRY = _descriptor.Descriptor(
  name='MapInputsEntry',
  full_name='pytorch.eas.PredictRequest.MapInputsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='pytorch.eas.PredictRequest.MapInputsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='pytorch.eas.PredictRequest.MapInputsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=452,
  serialized_end=525,
)

_PREDICTREQUEST = _descriptor.Descriptor(
  name='PredictRequest',
  full_name='pytorch.eas.PredictRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='inputs', full_name='pytorch.eas.PredictRequest.inputs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='output_filter', full_name='pytorch.eas.PredictRequest.output_filter', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='map_inputs', full_name='pytorch.eas.PredictRequest.map_inputs', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='debug_level', full_name='pytorch.eas.PredictRequest.debug_level', index=3,
      number=100, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_PREDICTREQUEST_MAPINPUTSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=285,
  serialized_end=525,
)


_PREDICTRESPONSE_MAPOUTPUTSENTRY = _descriptor.Descriptor(
  name='MapOutputsEntry',
  full_name='pytorch.eas.PredictResponse.MapOutputsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='pytorch.eas.PredictResponse.MapOutputsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='pytorch.eas.PredictResponse.MapOutputsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=656,
  serialized_end=730,
)

_PREDICTRESPONSE = _descriptor.Descriptor(
  name='PredictResponse',
  full_name='pytorch.eas.PredictResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='outputs', full_name='pytorch.eas.PredictResponse.outputs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='map_outputs', full_name='pytorch.eas.PredictResponse.map_outputs', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_PREDICTRESPONSE_MAPOUTPUTSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=528,
  serialized_end=730,
)

_ARRAYPROTO.fields_by_name['dtype'].enum_type = _ARRAYDATATYPE
_ARRAYPROTO.fields_by_name['array_shape'].message_type = _ARRAYSHAPE
_PREDICTREQUEST_MAPINPUTSENTRY.fields_by_name['value'].message_type = _ARRAYPROTO
_PREDICTREQUEST_MAPINPUTSENTRY.containing_type = _PREDICTREQUEST
_PREDICTREQUEST.fields_by_name['inputs'].message_type = _ARRAYPROTO
_PREDICTREQUEST.fields_by_name['map_inputs'].message_type = _PREDICTREQUEST_MAPINPUTSENTRY
_PREDICTRESPONSE_MAPOUTPUTSENTRY.fields_by_name['value'].message_type = _ARRAYPROTO
_PREDICTRESPONSE_MAPOUTPUTSENTRY.containing_type = _PREDICTRESPONSE
_PREDICTRESPONSE.fields_by_name['outputs'].message_type = _ARRAYPROTO
_PREDICTRESPONSE.fields_by_name['map_outputs'].message_type = _PREDICTRESPONSE_MAPOUTPUTSENTRY
DESCRIPTOR.message_types_by_name['ArrayShape'] = _ARRAYSHAPE
DESCRIPTOR.message_types_by_name['ArrayProto'] = _ARRAYPROTO
DESCRIPTOR.message_types_by_name['PredictRequest'] = _PREDICTREQUEST
DESCRIPTOR.message_types_by_name['PredictResponse'] = _PREDICTRESPONSE
DESCRIPTOR.enum_types_by_name['ArrayDataType'] = _ARRAYDATATYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ArrayShape = _reflection.GeneratedProtocolMessageType('ArrayShape', (_message.Message,), dict(
  DESCRIPTOR = _ARRAYSHAPE,
  __module__ = 'pytorch_predict_pb2'
  # @@protoc_insertion_point(class_scope:pytorch.eas.ArrayShape)
  ))
_sym_db.RegisterMessage(ArrayShape)

ArrayProto = _reflection.GeneratedProtocolMessageType('ArrayProto', (_message.Message,), dict(
  DESCRIPTOR = _ARRAYPROTO,
  __module__ = 'pytorch_predict_pb2'
  # @@protoc_insertion_point(class_scope:pytorch.eas.ArrayProto)
  ))
_sym_db.RegisterMessage(ArrayProto)

PredictRequest = _reflection.GeneratedProtocolMessageType('PredictRequest', (_message.Message,), dict(

  MapInputsEntry = _reflection.GeneratedProtocolMessageType('MapInputsEntry', (_message.Message,), dict(
    DESCRIPTOR = _PREDICTREQUEST_MAPINPUTSENTRY,
    __module__ = 'pytorch_predict_pb2'
    # @@protoc_insertion_point(class_scope:pytorch.eas.PredictRequest.MapInputsEntry)
    ))
  ,
  DESCRIPTOR = _PREDICTREQUEST,
  __module__ = 'pytorch_predict_pb2'
  # @@protoc_insertion_point(class_scope:pytorch.eas.PredictRequest)
  ))
_sym_db.RegisterMessage(PredictRequest)
_sym_db.RegisterMessage(PredictRequest.MapInputsEntry)

PredictResponse = _reflection.GeneratedProtocolMessageType('PredictResponse', (_message.Message,), dict(

  MapOutputsEntry = _reflection.GeneratedProtocolMessageType('MapOutputsEntry', (_message.Message,), dict(
    DESCRIPTOR = _PREDICTRESPONSE_MAPOUTPUTSENTRY,
    __module__ = 'pytorch_predict_pb2'
    # @@protoc_insertion_point(class_scope:pytorch.eas.PredictResponse.MapOutputsEntry)
    ))
  ,
  DESCRIPTOR = _PREDICTRESPONSE,
  __module__ = 'pytorch_predict_pb2'
  # @@protoc_insertion_point(class_scope:pytorch.eas.PredictResponse)
  ))
_sym_db.RegisterMessage(PredictResponse)
_sym_db.RegisterMessage(PredictResponse.MapOutputsEntry)


DESCRIPTOR._options = None
_ARRAYSHAPE.fields_by_name['dim']._options = None
_ARRAYPROTO.fields_by_name['float_val']._options = None
_ARRAYPROTO.fields_by_name['double_val']._options = None
_ARRAYPROTO.fields_by_name['int_val']._options = None
_ARRAYPROTO.fields_by_name['int64_val']._options = None
_PREDICTREQUEST_MAPINPUTSENTRY._options = None
_PREDICTRESPONSE_MAPOUTPUTSENTRY._options = None
# @@protoc_insertion_point(module_scope)
