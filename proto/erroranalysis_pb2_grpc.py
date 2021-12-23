# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


class QualityServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.errorAnalysis = channel.unary_unary(
        '/com.ices.sh.quality.rpc.QualityService/errorAnalysis',
        request_serializer=google_dot_protobuf_dot_wrappers__pb2.StringValue.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_wrappers__pb2.StringValue.FromString,
        )


class QualityServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def errorAnalysis(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_QualityServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'errorAnalysis': grpc.unary_unary_rpc_method_handler(
          servicer.errorAnalysis,
          request_deserializer=google_dot_protobuf_dot_wrappers__pb2.StringValue.FromString,
          response_serializer=google_dot_protobuf_dot_wrappers__pb2.StringValue.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'com.ices.sh.quality.rpc.QualityService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))