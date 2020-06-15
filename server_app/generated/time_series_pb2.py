# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: time_series.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='time_series.proto',
  package='time_series',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x11time_series.proto\x12\x0btime_series\"\x13\n\x11TimeSeriesRequest\"}\n\x0fTimeSeriesReply\x12;\n\x0b\x64\x61ta_points\x18\x01 \x03(\x0b\x32&.time_series.TimeSeriesReply.DataPoint\x1a-\n\tDataPoint\x12\x0c\n\x04time\x18\x01 \x01(\t\x12\x12\n\nmeterusage\x18\x02 \x01(\x02\x32U\n\nTimeSeries\x12G\n\x05Reply\x12\x1e.time_series.TimeSeriesRequest\x1a\x1c.time_series.TimeSeriesReply\"\x00\x62\x06proto3'
)




_TIMESERIESREQUEST = _descriptor.Descriptor(
  name='TimeSeriesRequest',
  full_name='time_series.TimeSeriesRequest',
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=34,
  serialized_end=53,
)


_TIMESERIESREPLY_DATAPOINT = _descriptor.Descriptor(
  name='DataPoint',
  full_name='time_series.TimeSeriesReply.DataPoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='time_series.TimeSeriesReply.DataPoint.time', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='meterusage', full_name='time_series.TimeSeriesReply.DataPoint.meterusage', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=135,
  serialized_end=180,
)

_TIMESERIESREPLY = _descriptor.Descriptor(
  name='TimeSeriesReply',
  full_name='time_series.TimeSeriesReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data_points', full_name='time_series.TimeSeriesReply.data_points', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TIMESERIESREPLY_DATAPOINT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=55,
  serialized_end=180,
)

_TIMESERIESREPLY_DATAPOINT.containing_type = _TIMESERIESREPLY
_TIMESERIESREPLY.fields_by_name['data_points'].message_type = _TIMESERIESREPLY_DATAPOINT
DESCRIPTOR.message_types_by_name['TimeSeriesRequest'] = _TIMESERIESREQUEST
DESCRIPTOR.message_types_by_name['TimeSeriesReply'] = _TIMESERIESREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TimeSeriesRequest = _reflection.GeneratedProtocolMessageType('TimeSeriesRequest', (_message.Message,), {
  'DESCRIPTOR' : _TIMESERIESREQUEST,
  '__module__' : 'time_series_pb2'
  # @@protoc_insertion_point(class_scope:time_series.TimeSeriesRequest)
  })
_sym_db.RegisterMessage(TimeSeriesRequest)

TimeSeriesReply = _reflection.GeneratedProtocolMessageType('TimeSeriesReply', (_message.Message,), {

  'DataPoint' : _reflection.GeneratedProtocolMessageType('DataPoint', (_message.Message,), {
    'DESCRIPTOR' : _TIMESERIESREPLY_DATAPOINT,
    '__module__' : 'time_series_pb2'
    # @@protoc_insertion_point(class_scope:time_series.TimeSeriesReply.DataPoint)
    })
  ,
  'DESCRIPTOR' : _TIMESERIESREPLY,
  '__module__' : 'time_series_pb2'
  # @@protoc_insertion_point(class_scope:time_series.TimeSeriesReply)
  })
_sym_db.RegisterMessage(TimeSeriesReply)
_sym_db.RegisterMessage(TimeSeriesReply.DataPoint)



_TIMESERIES = _descriptor.ServiceDescriptor(
  name='TimeSeries',
  full_name='time_series.TimeSeries',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=182,
  serialized_end=267,
  methods=[
  _descriptor.MethodDescriptor(
    name='Reply',
    full_name='time_series.TimeSeries.Reply',
    index=0,
    containing_service=None,
    input_type=_TIMESERIESREQUEST,
    output_type=_TIMESERIESREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TIMESERIES)

DESCRIPTOR.services_by_name['TimeSeries'] = _TIMESERIES

# @@protoc_insertion_point(module_scope)
