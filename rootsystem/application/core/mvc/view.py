# -*- coding: utf-8 -*-
from re import compile
from string import Template

from core.headers import header
from core.helper import read_file


class View(object):

    def render_template(self, tittle, content, folder=''):
        template = read_file('{}/template'.format(folder))
        dictionary = {
            'TITTLE': tittle,
            'CONTENT': content,
        }
        header.append(header.HTML)
        header.send()
        render = Template(template).safe_substitute(dictionary)
        return render

    def render_wait(self, url, time, message):
        base = read_file("wait")
        dictionary = {'url': url, 'time': time, 'message': message}
        header.append(header.HTML)
        header.send()
        render = Template(base).safe_substitute(dictionary)
        return render

    def get_match(self, template, tag):
        regex = compile("<!--%s-->(.|\n){1,}<!--%s-->" % (tag, tag))
        match = regex.search(template).group(0)
        return match

    def render_regex(self, template, tag, collection):
        match = self.get_match(template, tag)
        string = []
        for obj in collection:
            dictionary = obj if isinstance(obj, dict) else vars(obj)
            render = Template(match).safe_substitute(dictionary)
            string.append(render)

        render = str('\n'.join(string))
        content = template.replace(match, render)
        return content.replace("<!--{}-->\n".format(tag), "")

    def extract(self, template, tag):
        regex = self.get_match(template, tag)
        return template.replace(regex, "")
