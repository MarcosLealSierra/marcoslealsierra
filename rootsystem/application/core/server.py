#-*- coding: utf-8 -*-
from os import stat
from cgi import FieldStorage
from subprocess import Popen, PIPE
from settings import PRIVATE_DIR, TMP_DIR


class ServerFile(object):

    def get_mime(self, file_content, file_name):
        # Save temp
        with open('{}/{}'.format(TMP_DIR, file_name), 'w') as f:
            f.write(file_content)

        # Get mime type
        path = "{}/{}".format(TMP_DIR, file_name)
        p = Popen(['file', path, '--mime-type'], stderr=PIPE, stdout=PIPE)
        mime = p.stdout.read().split(': ')[1][:-1]
        return mime

    def upload(self, file_content, file_name, path=PRIVATE_DIR):
        with open('{}/{}'.format(path, file_name), 'w') as f:
            f.write(file_content)
        return file_content

    def upload_img(self, file_content, file_name, path=PRIVATE_DIR):
        with open('{}/{}'.format(path, file_name), 'wb') as f:
            f.write(file_content)
        return file_content

    def get_size(self, file_content, file_name):
        # Save temp
        with open('{}/{}'.format(TMP_DIR, file_name), 'w') as f:
            f.write(file_content)

        # Get file size
        f = "{}/{}".format(TMP_DIR, file_name)
        statinfo = stat(f)
        return statinfo.st_size

