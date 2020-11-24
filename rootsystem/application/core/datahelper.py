from core.db import DBQuery

from config import DB_NAME

class DataHelper(object):

    @staticmethod
    def get_scheme(table):
        sql = """SELECT COLUMN_NAME
                 FROM   INFORMATION_SCHEMA.COLUMNS
                 WHERE  TABLE_SCHEMA = '{}'
                 AND    TABLE_NAME = '{}'
                 """.format(DB_NAME, table)
        return DBQuery().execute(sql)

    @staticmethod
    def explode_scheme(table):
        scheme = DataHelper.get_scheme(table)
        columns = []
        for col in scheme:
            col = ','.join(col)
            columns.append(col)
        fields = ','.join(columns)
        return fields

    @staticmethod
    def set_query(table, where=None, type='LATEST'):
        str_fields = DataHelper.explode_scheme(table)
        sql = "SELECT {} FROM {}".format(str_fields, table)
        if where is not None:
            sql += " WHERE {}".format(where)
        if type == 'LATEST':
            sql += " ORDER BY {}_id DESC LIMIT ?".format(table)
        return sql
