from core.datahelper import DataHelper
from core.db import DBQuery
from core.helper import ucwords

DH_FILTER_EQ = '='
DH_FILTER_NOTEQ = '<>'
DH_FILTER_LT = '<'
DH_FILTER_GT = '>'

DH_FORMAT_DATA = 'data'
DH_FORMAT_OBJECT = 'object'


class DataHandler(object):

    def __init__(self, table='', data_format=''):
        self.table = ''.format(table)
        self.data_fomat = '{}'.format(DH_FORMAT_DATA)

    def get_latest(self, table, n=1):
        sql = str(DataHelper.set_query(table))
        sql = sql.replace('?', str(n))
        print sql

    def data2object(data):
        cls = ucwords(self.table)
        for values in data:
			var_id = '{}_id'.format(self.table)
			array = Factory.make(cls, var_id)

