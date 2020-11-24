# -*- coding: utf-8 -*-
from cgi import FieldStorage
from os import environ

#DB_HOST = 'localhost'
#DB_USER = 'hablemosdeazucar'
#DB_PASS = 'mrqJoBiwECmMCAsPVK4UUxsc'
#DB_NAME = 'hablemosdeazucarcgi'
#db_data = [DB_HOST, DB_USER, DB_PASS, DB_NAME]

POST = FieldStorage()
DOCUMENT_ROOT = '/srv/websites/marcoslealsierra/rootsystem'
PRIVATE_DIR = DOCUMENT_ROOT.replace('rootsystem', 'private')
TMP_DIR = "/tmp"
LOG_FILE = '{}/logs/marcoslealsierra.log'.format(PRIVATE_DIR)

DEFAULT_RESOURCE = "/page/inicio"
SHOW_ERROR_404 = False  # Produccion, muestra el recurso por defualt en la raiz
STATIC_DIR = "{}/static".format(DOCUMENT_ROOT)
TEMPLATE_FILE = "{}/html/template.html".format(STATIC_DIR)
URLS_FILE = '{}/urls'.format(PRIVATE_DIR)

# Directorio de sesiones (crear a mano si no existe)
#SESS_DIR = "{}/pysessions".format(PRIVATE_DIR)
#LOGIN_PAGE = "/credencial/login"

# Pagina de acceso restringido
#RESTRICTED_PAGE = "/page/restricted-page"

# Diccionario de diccionarios para el manejo de los mensajes de error
APP_ERRORS = dict()

APP_ERRORS['USER'] = dict(
    user='El usuario no puede estar vacio',
    name="El nombre completo es requerido",
    level='El nivel de acceso es requerido',
    email='El email no puede estar vacio',
    password='La contraseña es requerida'
)

APP_ERRORS['URLS'] = dict(
    url_amigable='La url no puede estar vacia',
    uri='La uri no puede estar vacia'
)

