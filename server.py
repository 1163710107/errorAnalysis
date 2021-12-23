import grpc
import time
from concurrent import futures
from Config.config import CONFIG
from google.protobuf import wrappers_pb2 as wrappers
from proto import erroranalysis_pb2 as error_analysis, erroranalysis_pb2_grpc as error_analysis_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
MAX_MESSAGE_LENGTH = 256 * 1024 * 1024


class QualityService(error_analysis_grpc.QualityServiceServicer):

    """
    @:param: request
    sample
    graph=request.value
    {nodes:[{id: 0, name:node0, meta_labels:node_type, other_attrs...}, {id: 1, name:node1, meta_labels:node_type, other_attrs...}],
    links:[{id: 0, directed:True/False, source_id: 0, source: node0, target_id: 1, target:node1, meta_labels: rel_type, relation: rel_name}]}
    @:return: the method should return errors format in different json structure for different error_type.
    entity name err:
        [{entid: num, error_name: string, correct_name:string, event_id: num, event:string},{},...]
    relation name err:
        [{rel_id:num, errorname: string, correct_name: string, event_id: num, event:string},{},...]
    link err & relation complete & data duplicated:
        [{sourceid: num, source_name: string, targetid: num, target_name:string, relid: num, rel_name: string}]
    attr complete:
        [{entid: num, ent_name: string, attr: string, value:string}]
    entity aligned:
        [{entid: num, similar_entities: [id1, id2,id3 ...]}]
    relation normalized:
        [{relid: num, similar_relations: [id1, id2,id3 ...]}]

    """
    def errorAnalysis(self, request: wrappers.StringValue, context):
        graph = request.value
        # todo
        errors = []
        return wrappers.StringValue(value=errors)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=CONFIG['grpc']['max_workers']), options=[
               ('grpc.max_send_message_length', MAX_MESSAGE_LENGTH),
               ('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH),
               ])
    error_analysis_grpc.add_QualityServiceServicer_to_server(
        QualityService(), server
    )
    port = CONFIG['grpc']['port']
    server.add_insecure_port('[::]:%d' % port)
    server.start()
    print('start serve on [::]:%d' % port)
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        print('stop serve...')
        server.stop(0)


if __name__ == '__main__':
    # test()
    serve()
