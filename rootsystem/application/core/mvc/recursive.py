#-*- coding: utf-8 -*-
from string import Template
from core.render import Template as myTemplate


class RecursiveObjectViewHelper:

    @staticmethod
    def get_stack(recursive_object, template, n=1, symbol="\t", stack=[]):
        dash = symbol * n

        for obj in recursive_object:
            collection = obj.__class__.__name__.lower()
            collection = "{}_collection".format(collection)
            dicc = vars(obj)
            dicc['n'] = dash
            stack.append(Template(template).safe_substitute(dicc))
            if hasattr(obj, collection):
                RecursiveObjectViewHelper.get_stack(
                        getattr(obj, collection), template, n + 1, symbol, stack)

        return stack
