from cgi import FieldStorage
#from email.mime.multipart import MIMEMultipart
#from email.mime.text import MIMEText
#from smtplib import SMTP
from string import Template
#from core.headers import header
from core.helper import read_file, Sanitizer, in_html
#from core.mvc.view import View
#from core.filters import Filter
from settings import HTTP_HTML, STATIC_DIR

class Page(object):
    pass


class PageView(object):

    def inicio(self):
        html = read_file('front/inicio')
        print(PageHelper.get_template(html, 'Inicio', 'index'))

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

    #def nosotros(self):
        #self.view.nosotros()

    #def atletas(self):
        #self.view.atletas()

    #def campanas(self):
        #self.view.campanas()

    #def mitos(self):
        #self.view.mitos()

    #def videos(self):
        #self.view.videos()

    #def contact_form(self):
        #form = FieldStorage()

        ## Get form data
        #nombre = Sanitizer.getval(form, 'nombre')
        #email = Sanitizer.getval(form, 'email')

        ## Filter form data
        #nombre = Filter.sanitize_string(nombre)
        #email = Filter.sanitize_string(email)

        #errors = {}

        ## Custom validation for inputs
        #if not len(nombre) >= 3:
            #errors['nombre'] = "El nombre no puede ser menor a 3 caracteres"

        #if Sanitizer.clean_email(email) == False:
            #errors['email'] = "El formato de correo es invalido"

        ##indice = Sanitizer.getval(form, 'RANDOM')
        ##with open("{}/questions".format(PRIVATE_DIR), 'r') as f:
            ##questions = f.read().split("\n")
        ##par = questions[int(indice)]
        ##pregunta, respuesta = list(par.split("|"))
        ##if not captcha == int(respuesta):
            ##errors['captcha'] = """La resolución de la suma es
                                    ##erronea o el campo esta en blanco,{} {}""".format(captcha, respuesta)

        #if errors:
            #errors = '<br>'.join(errors.values())
            #self.view.wait('/', 5, errors)
            #exit()

        ## Make dict with data for the email content
        #data = {
                #'nombre':nombre,
                #'email': email,
                #}

        ## Get email content in html
        #message = self.get_email_contact_html(data)

        ## Make a dict for send email
        #email_data = {
                #'to':['Ellery Eng<e@sembei.mx>',
                      #'marcos@sembei.mx'],
                #'subject':"Mesaje del formulario de contacto",
                #'reply_to':email,
                #'message': message
        #}
        #self.send_email(email_data)
        ## TODO make beauty render wait

        #sql = """
            #INSERT INTO     form
                            #(nombre, email)
            #VALUES          ('{}', '{}')
        #""".format(
            #data['nombre'], data['email'])

        #form_id = DBQuery().execute(sql)

    #def get_email_contact_html(self, data):
        #html = read_file('email/contact_form')
        #content = Template(html).safe_substitute(data)
        #return content

    #def send_email(self, data):
        #sender = 'Expo Carnes y Lácteos <{}>'.format(EMAIL_USER)
        #msg = MIMEMultipart("alternative")
        #msg['Subject'] = data['subject']
        #msg['From'] = sender
        #msg['to'] = ', '.join(data['to'])
        #msg['Reply-To'] = data['reply_to']
        #message = MIMEText(data['message'], 'html', 'utf-8')
        #msg.attach(message)
        #try:
            #mail = SMTP(SMTP_HOST, SMTP_PORT)
            #mail.ehlo()
            #mail.starttls()
            #mail.login(EMAIL_USER, EMAIL_PASS)
            #mail.sendmail(sender, data['to'], msg.as_string())
            #mail.quit()
            #mensaje = "Mensaje enviado correctamente"
            #self.view.wait('/', 5, mensaje)
        #except Exception as e:
            #url = '/'
            #mensaje = """
               #<h2> Lo sentimos, ocurrio un error en nuestro servidor
                #intentalo mas tarde {}</h2>
            #""".format(e)
            #self.view.wait(url, 4, mensaje)

    #def contact_form(self):
        #form = FieldStorage()
        #self.send_email(form)
        #self.send_email_user(form)

    #def get_html(self, form):
        #nombre = Sanitizer.getval(form, 'nombre')
        #apellidos =  Sanitizer.getval(form, 'apellidos')
        #nacimiento = Sanitizer.getval(form, 'nacimiento')
        #personas = Sanitizer.getval(form, 'personas')
        #correo = Sanitizer.getval(form, 'correo')
        #telefono = Sanitizer.getval(form, 'telefono')
        #embarcacion = Sanitizer.getval(form, 'embarcacion')
        #cabina = Sanitizer.getval(form, 'cabina')
        #perfiles = Sanitizer.getval(form, 'perfiles')
        #datos = Sanitizer.getval(form, 'datos')

        #diccionario = {
            #'nombre': nombre,
            #'apellidos': apellidos,
            #'nacimiento': nacimiento,
            #'personas': personas,
            #'correo': correo,
            #'telefono': telefono,
            #'embarcacion': embarcacion,
            #'cabina': cabina,
            #'perfiles': perfiles,
            #'datos': datos
        #}

        #html = read_file('email/email_template')
        #html = Template(html).safe_substitute(diccionario)
        #return html

    #def send_email_user(self, form):
        #html = read_file('email/email_user')
        #nombre = Sanitizer.getval(form, 'nombre')
        #apellidos = Sanitizer.getval(form, 'apellidos')
        #correo = Sanitizer.getval(form, 'correo')

        #nombre = Filter.sanitize_string(nombre)
        #apellidos = Filter.sanitize_string(apellidos)
        #correo = Filter.sanitize_string(correo).replace(" ", '').lower()

        #dic = {
            #'nombre': nombre,
            #'apellidos': apellidos
        #}

        #html = Template(html).safe_substitute(dic)

        #receiver = ['{} {} <{}>'.format(nombre, apellidos, correo)]
        #sender = "The Yachtsetter <contactemailapps@gmail.com>"

        #msg = MIMEMultipart("alternative")
        #msg['Subject'] = "Hola {} {}. Bienvenido a The Yachtsetter".format(nombre, apellidos)
        #msg['From'] = sender
        #msg['to'] = ', '.join(receiver)
        #msg['Reply-To'] = 'info@theyachtsetter.com'
        #message = MIMEText(html, 'html', 'utf-8')
        #msg.attach(message)
        #try:
            #mail = SMTP('smtp.gmail.com', 587)
            #mail.ehlo()
            #mail.starttls()
            #mail.login('contactemailapps@gmail.com', '*1Nt3nt4l0din')
            #mail.sendmail(sender, receiver, msg.as_string())
            #mail.quit()
        #except Exception as e:
            #exit()

    #def send_email(self, form):
        #html = self.get_html(form)
        #nombre = Sanitizer.getval(form, 'nombre')
        #apellidos = Sanitizer.getval(form, 'apellidos')
        #correo = Sanitizer.getval(form, 'correo')

        #nombre = Filter.sanitize_string(nombre)
        #apellidos = Filter.sanitize_string(apellidos)
        #correo = Filter.sanitize_string(correo).replace(" ", '').lower()

        #receiver = ['The Yachtsetter <info@theyachtsetter.com>']
        #sender = "The Yachtsetter <contactemailapps@gmail.com>"

        #msg = MIMEMultipart("alternative")
        #msg['Subject'] = "Nueva reserva de {} {}".format(nombre, apellidos)
        #msg['From'] = sender
        #msg['to'] = ', '.join(receiver)
        #msg['Reply-To'] = 'info@theyachtsetter.com'
        #message = MIMEText(html, 'html', 'utf-8')
        #msg.attach(message)
        #try:
            #mail = SMTP('smtp.gmail.com', 587)
            #mail.ehlo()
            #mail.starttls()
            #mail.login('contactemailapps@gmail.com', '*1Nt3nt4l0din')
            #mail.sendmail(sender, receiver, msg.as_string())
            #mail.quit()
            #url = '/'
            #mensaje = """
                #<h2>¡Gracias por tu interés <span>{} {} </span>en <strong>
                #The Yachtsetter: <span>Baja Experience!</span></strong></h2>
                #<p>Como sabes, TYS es un evento privado con cupo limitado.
                #En un máximo de 72 horas te confirmaremos si contamos con espacio para tu asistencia.</p>
                #<p><strong>TYS</strong></p>
            #""".format(nombre, apellidos)
            #self.view.wait(url, 5, mensaje)
        #except Exception as e:
            #url = '/'
            #mensaje = """
               #<h2> Lo sentimos, ocurrio un error en nuestro servidor
                #intentalo mas tarde {}</h2>
            #""".format(e)
            #self.view.wait(url, 4, mensaje)


class PageHelper(object):

    @staticmethod
    def get_template(html, title='', script_name='default'):
        content = View().render_template(title, html)
        script_file = read_file('front/scripts')
        script = View().get_match(script_file, script_name)
        dic = {'SCRIPT':script}
        render = Template(content).safe_substitute(dic)
        return render
