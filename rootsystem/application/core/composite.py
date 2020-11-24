#TODO reemplazar exec por __import__(ver xfc)

class Composite(object):

    def __init__(self, cls_name):
        clslower = cls_name.lower()
        # module = __import__("modules.{}".format(clslower), fromlist=[cls_name])
        exec("from modules.{} import {}".format(clslower, cls_name))
        self.clase = locals()[cls_name]

    def compose(self, obj):
        if isinstance(obj, self.clase) or obj is None:
            return obj
        else:
            current = str(type(obj))
            expected = self.clase.__name__
            msg = "{} is not an instance of {}".format(current, expected)
            raise TypeError(msg)
