# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: orderer/ab.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common import common_pb2 as common_dot_common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='orderer/ab.proto',
  package='orderer',
  syntax='proto3',
  serialized_pb=_b('\n\x10orderer/ab.proto\x12\x07orderer\x1a\x13\x63ommon/common.proto\"3\n\x11\x42roadcastResponse\x12\x1e\n\x06status\x18\x01 \x01(\x0e\x32\x0e.common.Status\"\x0c\n\nSeekNewest\"\x0c\n\nSeekOldest\"\x1f\n\rSeekSpecified\x12\x0e\n\x06number\x18\x01 \x01(\x04\"\x91\x01\n\x0cSeekPosition\x12%\n\x06newest\x18\x01 \x01(\x0b\x32\x13.orderer.SeekNewestH\x00\x12%\n\x06oldest\x18\x02 \x01(\x0b\x32\x13.orderer.SeekOldestH\x00\x12+\n\tspecified\x18\x03 \x01(\x0b\x32\x16.orderer.SeekSpecifiedH\x00\x42\x06\n\x04Type\"\xc5\x01\n\x08SeekInfo\x12$\n\x05start\x18\x01 \x01(\x0b\x32\x15.orderer.SeekPosition\x12#\n\x04stop\x18\x02 \x01(\x0b\x32\x15.orderer.SeekPosition\x12\x30\n\x08\x62\x65havior\x18\x03 \x01(\x0e\x32\x1e.orderer.SeekInfo.SeekBehavior\"<\n\x0cSeekBehavior\x12\x15\n\x11\x42LOCK_UNTIL_READY\x10\x00\x12\x15\n\x11\x46\x41IL_IF_NOT_READY\x10\x01\"[\n\x0f\x44\x65liverResponse\x12 \n\x06status\x18\x01 \x01(\x0e\x32\x0e.common.StatusH\x00\x12\x1e\n\x05\x62lock\x18\x02 \x01(\x0b\x32\r.common.BlockH\x00\x42\x06\n\x04Type2\x8f\x01\n\x0f\x41tomicBroadcast\x12?\n\tBroadcast\x12\x10.common.Envelope\x1a\x1a.orderer.BroadcastResponse\"\x00(\x01\x30\x01\x12;\n\x07\x44\x65liver\x12\x10.common.Envelope\x1a\x18.orderer.DeliverResponse\"\x00(\x01\x30\x01\x42U\n%org.hyperledger.fabric.protos.ordererZ,github.com/foglink/fnkcore/src/protos/ordererb\x06proto3')
  ,
  dependencies=[common_dot_common__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_SEEKINFO_SEEKBEHAVIOR = _descriptor.EnumDescriptor(
  name='SeekBehavior',
  full_name='orderer.SeekInfo.SeekBehavior',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BLOCK_UNTIL_READY', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAIL_IF_NOT_READY', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=450,
  serialized_end=510,
)
_sym_db.RegisterEnumDescriptor(_SEEKINFO_SEEKBEHAVIOR)


_BROADCASTRESPONSE = _descriptor.Descriptor(
  name='BroadcastResponse',
  full_name='orderer.BroadcastResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='orderer.BroadcastResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=50,
  serialized_end=101,
)


_SEEKNEWEST = _descriptor.Descriptor(
  name='SeekNewest',
  full_name='orderer.SeekNewest',
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=103,
  serialized_end=115,
)


_SEEKOLDEST = _descriptor.Descriptor(
  name='SeekOldest',
  full_name='orderer.SeekOldest',
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=117,
  serialized_end=129,
)


_SEEKSPECIFIED = _descriptor.Descriptor(
  name='SeekSpecified',
  full_name='orderer.SeekSpecified',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='number', full_name='orderer.SeekSpecified.number', index=0,
      number=1, type=4, cpp_type=4, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=131,
  serialized_end=162,
)


_SEEKPOSITION = _descriptor.Descriptor(
  name='SeekPosition',
  full_name='orderer.SeekPosition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='newest', full_name='orderer.SeekPosition.newest', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='oldest', full_name='orderer.SeekPosition.oldest', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='specified', full_name='orderer.SeekPosition.specified', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='Type', full_name='orderer.SeekPosition.Type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=165,
  serialized_end=310,
)


_SEEKINFO = _descriptor.Descriptor(
  name='SeekInfo',
  full_name='orderer.SeekInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start', full_name='orderer.SeekInfo.start', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stop', full_name='orderer.SeekInfo.stop', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='behavior', full_name='orderer.SeekInfo.behavior', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SEEKINFO_SEEKBEHAVIOR,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=313,
  serialized_end=510,
)


_DELIVERRESPONSE = _descriptor.Descriptor(
  name='DeliverResponse',
  full_name='orderer.DeliverResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='orderer.DeliverResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='block', full_name='orderer.DeliverResponse.block', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='Type', full_name='orderer.DeliverResponse.Type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=512,
  serialized_end=603,
)

_BROADCASTRESPONSE.fields_by_name['status'].enum_type = common_dot_common__pb2._STATUS
_SEEKPOSITION.fields_by_name['newest'].message_type = _SEEKNEWEST
_SEEKPOSITION.fields_by_name['oldest'].message_type = _SEEKOLDEST
_SEEKPOSITION.fields_by_name['specified'].message_type = _SEEKSPECIFIED
_SEEKPOSITION.oneofs_by_name['Type'].fields.append(
  _SEEKPOSITION.fields_by_name['newest'])
_SEEKPOSITION.fields_by_name['newest'].containing_oneof = _SEEKPOSITION.oneofs_by_name['Type']
_SEEKPOSITION.oneofs_by_name['Type'].fields.append(
  _SEEKPOSITION.fields_by_name['oldest'])
_SEEKPOSITION.fields_by_name['oldest'].containing_oneof = _SEEKPOSITION.oneofs_by_name['Type']
_SEEKPOSITION.oneofs_by_name['Type'].fields.append(
  _SEEKPOSITION.fields_by_name['specified'])
_SEEKPOSITION.fields_by_name['specified'].containing_oneof = _SEEKPOSITION.oneofs_by_name['Type']
_SEEKINFO.fields_by_name['start'].message_type = _SEEKPOSITION
_SEEKINFO.fields_by_name['stop'].message_type = _SEEKPOSITION
_SEEKINFO.fields_by_name['behavior'].enum_type = _SEEKINFO_SEEKBEHAVIOR
_SEEKINFO_SEEKBEHAVIOR.containing_type = _SEEKINFO
_DELIVERRESPONSE.fields_by_name['status'].enum_type = common_dot_common__pb2._STATUS
_DELIVERRESPONSE.fields_by_name['block'].message_type = common_dot_common__pb2._BLOCK
_DELIVERRESPONSE.oneofs_by_name['Type'].fields.append(
  _DELIVERRESPONSE.fields_by_name['status'])
_DELIVERRESPONSE.fields_by_name['status'].containing_oneof = _DELIVERRESPONSE.oneofs_by_name['Type']
_DELIVERRESPONSE.oneofs_by_name['Type'].fields.append(
  _DELIVERRESPONSE.fields_by_name['block'])
_DELIVERRESPONSE.fields_by_name['block'].containing_oneof = _DELIVERRESPONSE.oneofs_by_name['Type']
DESCRIPTOR.message_types_by_name['BroadcastResponse'] = _BROADCASTRESPONSE
DESCRIPTOR.message_types_by_name['SeekNewest'] = _SEEKNEWEST
DESCRIPTOR.message_types_by_name['SeekOldest'] = _SEEKOLDEST
DESCRIPTOR.message_types_by_name['SeekSpecified'] = _SEEKSPECIFIED
DESCRIPTOR.message_types_by_name['SeekPosition'] = _SEEKPOSITION
DESCRIPTOR.message_types_by_name['SeekInfo'] = _SEEKINFO
DESCRIPTOR.message_types_by_name['DeliverResponse'] = _DELIVERRESPONSE

BroadcastResponse = _reflection.GeneratedProtocolMessageType('BroadcastResponse', (_message.Message,), dict(
  DESCRIPTOR = _BROADCASTRESPONSE,
  __module__ = 'orderer.ab_pb2'
  # @@protoc_insertion_point(class_scope:orderer.BroadcastResponse)
  ))
_sym_db.RegisterMessage(BroadcastResponse)

SeekNewest = _reflection.GeneratedProtocolMessageType('SeekNewest', (_message.Message,), dict(
  DESCRIPTOR = _SEEKNEWEST,
  __module__ = 'orderer.ab_pb2'
  # @@protoc_insertion_point(class_scope:orderer.SeekNewest)
  ))
_sym_db.RegisterMessage(SeekNewest)

SeekOldest = _reflection.GeneratedProtocolMessageType('SeekOldest', (_message.Message,), dict(
  DESCRIPTOR = _SEEKOLDEST,
  __module__ = 'orderer.ab_pb2'
  # @@protoc_insertion_point(class_scope:orderer.SeekOldest)
  ))
_sym_db.RegisterMessage(SeekOldest)

SeekSpecified = _reflection.GeneratedProtocolMessageType('SeekSpecified', (_message.Message,), dict(
  DESCRIPTOR = _SEEKSPECIFIED,
  __module__ = 'orderer.ab_pb2'
  # @@protoc_insertion_point(class_scope:orderer.SeekSpecified)
  ))
_sym_db.RegisterMessage(SeekSpecified)

SeekPosition = _reflection.GeneratedProtocolMessageType('SeekPosition', (_message.Message,), dict(
  DESCRIPTOR = _SEEKPOSITION,
  __module__ = 'orderer.ab_pb2'
  # @@protoc_insertion_point(class_scope:orderer.SeekPosition)
  ))
_sym_db.RegisterMessage(SeekPosition)

SeekInfo = _reflection.GeneratedProtocolMessageType('SeekInfo', (_message.Message,), dict(
  DESCRIPTOR = _SEEKINFO,
  __module__ = 'orderer.ab_pb2'
  # @@protoc_insertion_point(class_scope:orderer.SeekInfo)
  ))
_sym_db.RegisterMessage(SeekInfo)

DeliverResponse = _reflection.GeneratedProtocolMessageType('DeliverResponse', (_message.Message,), dict(
  DESCRIPTOR = _DELIVERRESPONSE,
  __module__ = 'orderer.ab_pb2'
  # @@protoc_insertion_point(class_scope:orderer.DeliverResponse)
  ))
_sym_db.RegisterMessage(DeliverResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n%org.hyperledger.fabric.protos.ordererZ,github.com/foglink/fnkcore/src/protos/orderer'))
try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces


  class AtomicBroadcastStub(object):

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.Broadcast = channel.stream_stream(
          '/orderer.AtomicBroadcast/Broadcast',
          request_serializer=common_dot_common__pb2.Envelope.SerializeToString,
          response_deserializer=BroadcastResponse.FromString,
          )
      self.Deliver = channel.stream_stream(
          '/orderer.AtomicBroadcast/Deliver',
          request_serializer=common_dot_common__pb2.Envelope.SerializeToString,
          response_deserializer=DeliverResponse.FromString,
          )


  class AtomicBroadcastServicer(object):

    def Broadcast(self, request_iterator, context):
      """broadcast receives a reply of Acknowledgement for each common.Envelope in order, indicating success or type of failure
      """
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def Deliver(self, request_iterator, context):
      """deliver first requires an Envelope of type DELIVER_SEEK_INFO with Payload data as a mashaled SeekInfo message, then a stream of block replies is received.
      """
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_AtomicBroadcastServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'Broadcast': grpc.stream_stream_rpc_method_handler(
            servicer.Broadcast,
            request_deserializer=common_dot_common__pb2.Envelope.FromString,
            response_serializer=BroadcastResponse.SerializeToString,
        ),
        'Deliver': grpc.stream_stream_rpc_method_handler(
            servicer.Deliver,
            request_deserializer=common_dot_common__pb2.Envelope.FromString,
            response_serializer=DeliverResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'orderer.AtomicBroadcast', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaAtomicBroadcastServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def Broadcast(self, request_iterator, context):
      """broadcast receives a reply of Acknowledgement for each common.Envelope in order, indicating success or type of failure
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def Deliver(self, request_iterator, context):
      """deliver first requires an Envelope of type DELIVER_SEEK_INFO with Payload data as a mashaled SeekInfo message, then a stream of block replies is received.
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaAtomicBroadcastStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def Broadcast(self, request_iterator, timeout, metadata=None, with_call=False, protocol_options=None):
      """broadcast receives a reply of Acknowledgement for each common.Envelope in order, indicating success or type of failure
      """
      raise NotImplementedError()
    def Deliver(self, request_iterator, timeout, metadata=None, with_call=False, protocol_options=None):
      """deliver first requires an Envelope of type DELIVER_SEEK_INFO with Payload data as a mashaled SeekInfo message, then a stream of block replies is received.
      """
      raise NotImplementedError()


  def beta_create_AtomicBroadcast_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('orderer.AtomicBroadcast', 'Broadcast'): common_dot_common__pb2.Envelope.FromString,
      ('orderer.AtomicBroadcast', 'Deliver'): common_dot_common__pb2.Envelope.FromString,
    }
    response_serializers = {
      ('orderer.AtomicBroadcast', 'Broadcast'): BroadcastResponse.SerializeToString,
      ('orderer.AtomicBroadcast', 'Deliver'): DeliverResponse.SerializeToString,
    }
    method_implementations = {
      ('orderer.AtomicBroadcast', 'Broadcast'): face_utilities.stream_stream_inline(servicer.Broadcast),
      ('orderer.AtomicBroadcast', 'Deliver'): face_utilities.stream_stream_inline(servicer.Deliver),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_AtomicBroadcast_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('orderer.AtomicBroadcast', 'Broadcast'): common_dot_common__pb2.Envelope.SerializeToString,
      ('orderer.AtomicBroadcast', 'Deliver'): common_dot_common__pb2.Envelope.SerializeToString,
    }
    response_deserializers = {
      ('orderer.AtomicBroadcast', 'Broadcast'): BroadcastResponse.FromString,
      ('orderer.AtomicBroadcast', 'Deliver'): DeliverResponse.FromString,
    }
    cardinalities = {
      'Broadcast': cardinality.Cardinality.STREAM_STREAM,
      'Deliver': cardinality.Cardinality.STREAM_STREAM,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'orderer.AtomicBroadcast', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
