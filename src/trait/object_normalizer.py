from json import JSONEncoder
import datetime


class Normalize(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        return obj.__dict__
