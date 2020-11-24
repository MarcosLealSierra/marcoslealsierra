import json


class APIRESTFul(object):

    def __init__(self, obj):
        self.json_data = '{}'
        if not isinstance(obj, str):
            self.json_data = self.dict2json(vars(obj))

    def obj2dict(self, obj):
        types = (str, int, float, bool, tuple, list, dict)
        for prop, value in obj.iteritems():
            notinstance = not isinstance(value, types)
            if notinstance and not value is None:
                obj[prop] = vars(value)
                sub = self.obj2dict(obj[prop])
                if not obj[prop] == sub:
                    obj[prop] = sub
        return obj

    def dict2json(self, obj):
        obj = json.dumps(self.obj2dict(obj), indent=4, sort_keys=True)
        return '\n'.join([line.rstrip() for line in obj.splitlines()])
