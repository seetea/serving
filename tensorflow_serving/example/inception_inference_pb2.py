# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: inception_inference.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='inception_inference.proto',
  package='tensorflow.serving',
  syntax='proto3',
  serialized_pb=b'\n\x19inception_inference.proto\x12\x12tensorflow.serving\"(\n\x10InceptionRequest\x12\x14\n\x0cjpeg_encoded\x18\x01 \x01(\x0c\"4\n\x11InceptionResponse\x12\x0f\n\x07\x63lasses\x18\x01 \x03(\x05\x12\x0e\n\x06scores\x18\x02 \x03(\x02\x32k\n\x10InceptionService\x12W\n\x08\x43lassify\x12$.tensorflow.serving.InceptionRequest\x1a%.tensorflow.serving.InceptionResponseb\x06proto3'
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_INCEPTIONREQUEST = _descriptor.Descriptor(
  name='InceptionRequest',
  full_name='tensorflow.serving.InceptionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='jpeg_encoded', full_name='tensorflow.serving.InceptionRequest.jpeg_encoded', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=49,
  serialized_end=89,
)


_INCEPTIONRESPONSE = _descriptor.Descriptor(
  name='InceptionResponse',
  full_name='tensorflow.serving.InceptionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='classes', full_name='tensorflow.serving.InceptionResponse.classes', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='scores', full_name='tensorflow.serving.InceptionResponse.scores', index=1,
      number=2, type=2, cpp_type=6, label=3,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=91,
  serialized_end=143,
)

DESCRIPTOR.message_types_by_name['InceptionRequest'] = _INCEPTIONREQUEST
DESCRIPTOR.message_types_by_name['InceptionResponse'] = _INCEPTIONRESPONSE

InceptionRequest = _reflection.GeneratedProtocolMessageType('InceptionRequest', (_message.Message,), dict(
  DESCRIPTOR = _INCEPTIONREQUEST,
  __module__ = 'inception_inference_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.serving.InceptionRequest)
  ))
_sym_db.RegisterMessage(InceptionRequest)

InceptionResponse = _reflection.GeneratedProtocolMessageType('InceptionResponse', (_message.Message,), dict(
  DESCRIPTOR = _INCEPTIONRESPONSE,
  __module__ = 'inception_inference_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.serving.InceptionResponse)
  ))
_sym_db.RegisterMessage(InceptionResponse)


import abc
from grpc.beta import implementations as beta_implementations
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

class BetaInceptionServiceServicer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def Classify(self, request, context):
    raise NotImplementedError()

class BetaInceptionServiceStub(object):
  """The interface to which stubs will conform."""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def Classify(self, request, timeout):
    raise NotImplementedError()
  Classify.future = None

def beta_create_InceptionService_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  import inception_inference_pb2
  import inception_inference_pb2
  request_deserializers = {
    ('tensorflow.serving.InceptionService', 'Classify'): inception_inference_pb2.InceptionRequest.FromString,
  }
  response_serializers = {
    ('tensorflow.serving.InceptionService', 'Classify'): inception_inference_pb2.InceptionResponse.SerializeToString,
  }
  method_implementations = {
    ('tensorflow.serving.InceptionService', 'Classify'): face_utilities.unary_unary_inline(servicer.Classify),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)

def beta_create_InceptionService_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  import inception_inference_pb2
  import inception_inference_pb2
  request_serializers = {
    ('tensorflow.serving.InceptionService', 'Classify'): inception_inference_pb2.InceptionRequest.SerializeToString,
  }
  response_deserializers = {
    ('tensorflow.serving.InceptionService', 'Classify'): inception_inference_pb2.InceptionResponse.FromString,
  }
  cardinalities = {
    'Classify': cardinality.Cardinality.UNARY_UNARY,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'tensorflow.serving.InceptionService', cardinalities, options=stub_options)
# @@protoc_insertion_point(module_scope)
