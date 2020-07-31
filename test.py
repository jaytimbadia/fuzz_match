import ingestor_pb2
from  similarity import get_match


def calculate(file):

    source = list(file.source)
    target = list(file.target)

    source_rt, target_rt, confidence_rt = get_match(source, target)
    if source_rt != []:

        myresponse = ingestor_pb2.response()
        myresponse.source.extend(source_rt)
        myresponse.target.extend(target_rt)
        myresponse.confidence.extend(confidence_rt)
        myresponse.SerializeToString()
    else:
        print('print some erorr occured')
        myresponse = ingestor_pb2.response()
        myresponse.source.extend(['Some error occured'])
        myresponse.target.extend([target_rt])
        myresponse.confidence.extend([confidence_rt])
        myresponse.SerializeToString()

    return myresponse

