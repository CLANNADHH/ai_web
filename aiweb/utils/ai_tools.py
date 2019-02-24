import json


def ai_json_dumps(*args, **kwargs):
    try:
        return json.dumps({"result": arg for arg in args})
    except Exception as error:
        return json.dumps({"Error": str(error)})


def ai_json_loads(*args, **kwargs):
    try:
        return json.loads(*args)
    except Exception as error:
        return json.dumps({"Error": str(error)})
