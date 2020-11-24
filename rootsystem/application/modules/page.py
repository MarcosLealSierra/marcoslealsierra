from cgi import FieldStorage
#from email.mime.multipart import MIMEMultipart
#from email.mime.text import MIMEText
#from smtplib import SMTP
from string import Template
#from core.headers import header
from core.helper import read_file, Sanitizer, in_html
from core.mvc.view import View
#from core.filters import Filter
from settings import HTTP_HTML, STATIC_DIR, TEMPLATE_FILE

class Page(object):
    pass


class PageView(View):

    def inicio(self):
        with open(TEMPLATE_FILE, "r") as f:
            index = f.read()

        #regex = "<!-- errores -->(.|\n)+<!-- errores -->"
        #form = sub(regex, '', form)

        print(HTTP_HTML)
        print("")
        print(index)
        #print(Template(TEMPLATE_PATH).render_inner(form))


    #def nosotros(self):
        #html = read_file("front/nosotros")
        #print(PageHelper.get_template(html, 'Nosotros'))

    #def atletas(self):
        #html = read_file("front/atletas")
        #print(PageHelper.get_template(html, 'Atletas'))

    #def campanas(self):
        #html = read_file("front/campanas")
        #print(PageHelper.get_template(html, 'Campañas'))

    #def mitos(self):
        #html = read_file("front/mitos")
        #print(PageHelper.get_template(html, 'Mitos'))

    #def videos(self):
        #html = read_file("front/videos")
        #print(PageHelper.get_template(html, 'Video', 'video'))

    #def wait(self, url, time, message):
        #print(self.render_wait(url, time, message))


class PageController(object):

    def __init__(self):
        self.model = Page()
        self.view = PageView()

    def inicio(self):
        self.view.inicio()
