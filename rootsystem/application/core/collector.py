#-*- coding: utf-8 -*-
from core.db import DBQuery


class CollectorObject(object):

    def __init__(self):
        self.collection = []

    def add_obj(self, obj):
        self.collection.append(obj)

    def get(self, cls_name):
        table = cls_name.lower()
        sql = "SELECT {}_id FROM {}".format(table, table)
        rows = DBQuery().execute(sql)
        exec("from modules.{} import {}".format(table, cls_name))

        for row in rows:
            obj = locals()[cls_name]()
            exec("obj.{}_id = '{}'".format(table, row[0]))
            obj.select()
            self.add_obj(obj)

        return self.collection
