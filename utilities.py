from rest_framework.response import Response
import datetime
import json


def makeJsonResponse(data, message, status_code):
    resp_data = {
        "error-message": message,
        "results": data
    }
    response = Response(resp_data, status=status_code)
    return response

def jsonSerialCustom(o):
    if isinstance(o, (datetime.datetime)):
        return str(o)

def dataSerializer(datas, *args):
    result = json.loads(json.dumps([dict(data) for data in datas.values()], sort_keys=True, indent=1, default=jsonSerialCustom))
    return result