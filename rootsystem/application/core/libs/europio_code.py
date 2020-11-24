#-*- coding: utf-8 -*-

"""
EuropioCode Python

Codificador y decodificador de caracteres para Python 2 y 3.

Codifica cadenas de texto convirtiendo caracteres no alfanuméricos en pseudo
codigo, sanitizando así, cualquier campo de formulario previo a su
envío. Luego, decodifica el pseudocódigo convirtiéndolo en entidades 
hexadecimales de HTML.
Utilizado de forma conjunta con ModSecurity y las reglas de OWASP,
lograrán formularios invulnerables con aplicaciones 100% funcionales, gracias
a su deodificador que interpretará el código de forma tal, que sean evitados
los falsos positivos de ModSecurity. 

(c) Copyright 2014, Eugenia Bahit
EuropioCode is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
EuropioCode is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with EuropioCode().  If not, see <http://www.gnu.org/licenses/>.


    Usage:
        Import:
            from europio_code import EuropioCode

        Encode a string to EuropioCode:
            new_string = EuropioCode().encode("<b>Hello 'world'.</b>")

            Produces this string (in one line):
            ECODG60ECODCbECODG62ECODCHelloECODG160ECODCECODG39ECODCworldECODG39
            ECODCECODG46ECODCECODG60ECODCECODG47ECODCbECODG62ECODC

        Convert an EuropioCode string to HTML entities:
            converted_string = EuropioCode().decode(new_string)

            Produces this HTML code:
            &#60;b&#62;Hello&#160;&#39;world&#39;&#46;&#60;&#47;b&#62;

"""
__author__ = "Eugenia Bahit <ebahit@member.fsf.org>"
__version__ = "1.0"

from re import sub
from sys import version_info
pyversion = version_info[0]


class EuropioCode(object):

    special_char_prefix = "ECOD"
    preformat_prefix = "pFt"

    def set_base_table(cls):
        """
            Establecer la tabla numérica de equivalencias para entidades html
            hexadecimales
        """
        cls.tbl01 = {
          '!': 33, "\"": 34, '#': 35, '$': 36, '%': 37, '&': 38, "'": 39,
          '(': 40, ')': 41, '*': 42, '+': 43, ',': 44, '.': 46, '/': 47,
          ':': 58, '<': 60, '=': 61, '>': 62, '?': 63, '@': 64, '[': 91,
          '\\': 92, ']': 93, '^': 94, '_': 95, '`': 96, '{': 123, '|': 124,
          '}': 125, '~': 126, '€': 128, ' ': 160, '¡': 161, '£': 163, '«': 171,
          '´': 180, '·': 183, '»': 187, '¿': 191, 'Ç': 199, 'ç': 231, '-': 45,
          ';': 59, '\n': 13, 'Á': 193, 'É': 201, 'Í': 205, 'Ó': 211, 'Ú': 218,
          'Ü': 220, 'á': 225, 'é': 233, 'í': 237, 'ó': 243, 'ú': 250, 'ü': 252,
          'Ñ': 209, 'ñ': 241
        }

    def set_preformat_table(cls):
        """
            Establecer la tabla de tags html permitidos en textos con preformato
        """
        cls.tbl02 = [
            '<b>', '<strong>', '<i>', '<em>', '<u>', 
            '<strike>', '<sub>', '<sup>',
            '<p>', '<blockquote>', '<hr>',
            '<ul>', '<ol>', '<li>',
            '<h1>', '<h2>', '<h3>', '<h4>', '<h5>', '<h6>',
            '<code>', '<pre>', '<br>', '<small>'
        ]

    def set_especial_chars_table(cls):
        """
            Establecer la tabla de codificación de caracteres de tratamiento
            especial
        """
        prefix = cls.special_char_prefix
        letters = ["%s%s" % (prefix, l) for l in ['G', 'C', 'S']]
        chars = ['&#', ';', "\n"]
        cls.tbl03 = dict(zip(letters, chars))

    def set_hyperlink_table(cls):
        """
            Establecer la tabla de codificación para hiperenlaces
        """
        cls.tbl04 = {
            '>': 'fT0x1', '"': '', '<a href=': 'aH0n2',
            'target=_': 'tG0n7', '://': 'pT7n3', '/': 'bB0n1',
            '~': 'nN0n5', '.': 'p01nt', '-': 'gN6n1'
        }

    def set_preserve_table(cls):
        """
            Establecer la tabla de caracteres no alfanuméricos a conservar en
            una limpieza
        """
        cls.tbl05 = {
            '&#225;': 'a', '&#233;': 'e', '&#237;': 'i', '&#243;': 'o',
            '&#250;': 'u', '&#252;': 'u',
            '&#193;': 'A', '&#201;': 'E', '&#205;': 'I', '&#211;': 'O',
            '&#218;': 'U', '&#220;': 'U',
            '&#241;': 'n', '&#209;': 'N',
            '&#231;': 'c', '&#199;': 'C', '&#160;': ' '
        }

# ******************************************************************************

    def encode(cls, cadena):
        """
            Codificar una cadena en formato EuropioCode desde su estado original

            Params:
                cadena -- la cadena a ser codificada

            Returns:
                resultado -- la cadena codificada
        """
        cls.set_base_table()
        prefix = cls.special_char_prefix

        resultado = cadena.replace("\n", "%sS" % prefix)

        for char, num in cls.__items__(cls.tbl01):
            code = "%sG%s%sC" % (prefix, num, prefix)
            resultado = resultado.replace(char, code)

        return resultado

    def decode(cls, cadena, tipo_salto=''):
        """
            Decodifica una cadena en formato EuropioCode a sus entidades HTML

            Params:
                cadena -- la cadena a ser decodificada
                tipo_salto -- (opcional) 'br' para aplicar etiquetas HTML

            Returns:
                cadena -- la cadena convertida a entidades HTML
        """
        cls.set_especial_chars_table()

        for clave, valor in cls.__items__(cls.tbl03):
            cadena = cadena.replace(clave, valor)

        pf = cls.preformat_prefix
        cadena = sub("%s(e)?[0-9]{1,2}" % pf, "", cadena)

        return sub("\n", "<br>", cadena) if tipo_salto == 'br' else cadena

    def __items__(cls, dic):
        return dic.iteritems() if pyversion < 3 else dic.items()

    def decode_hyperlink(cls, cadena):
        cls.set_hyperlink_table();

        res = cadena.replace(
            cls.tbl04.values(),
            cls.tbl04.keys()
        )
        return res.replace("eT0n1", "</a>")

    def decode_preformat(cls, cadena):
        cls.set_preformat_table()

        # resultado = cls.decode_hyperlink(cadena)
        resultado = cadena
        for i, char in enumerate(cls.tbl02):
            numero = "0i" if i < 10 else i

            pft_apertura = "{}{}".format(cls.preformat_prefix, numero)
            tag_apertura = cls.tbl02[i]
            resultado = resultado.replace(pft_apertura, tag_apertura)

            pft_cierre = "{}e{}".format(cls.preformat_prefix, numero)
            tag_cierre = tag_apertura.replace("<", "</")
            resultado = resultado.replace(pft_cierre, tag_cierre)


        decode = cls.decode(resultado)
        return decode.replace("&#160", " ")

