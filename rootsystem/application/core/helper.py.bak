from datetime import date, time
import re
from core.headers import header
from settings import APP_ERRORS, STATIC_DIR, HTTP_HTML


class FilesHelper:

    @staticmethod
    def read_file(filename):
        """Read file
                Params:
                        filename -- (string) File path to be read
                Returns:
                        content -- (string) Text string with the content read
        """
        file_path = '{}/html/{}.html'.format(STATIC_DIR, filename)
        with open(file_path, 'r') as tmp:
                content = tmp.read()
        return content

    @staticmethod
    def in_html(content):
        """ In HTML
                Params:
                        content -- any content that you want: string, int,
                        object etc.
                Return:
                        Content that you pass through the params in html page,
                        printing headers
        """
        header.append(header.HTML)
        header.send()
        print(content)

class Sanitizer:

    @staticmethod
    def getval(form, key):
        def wrapper():
            return form[key].value if key in form else ''
        return '' if form is None else wrapper()

    @staticmethod
    def clean_email(email):
        """Eval email format
				Params:
						email -- (string) to be cleaned
				Returns:
						string -- cleaned
        """
        new_email = email.lower()
        valid_chars = ["@", ".", "-", "_", "+"]
        for char in email:
                if not char.isalnum() and not char in valid_chars:
                        new_email = new_email.replace(char, "")
        if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',new_email):
                return new_email
        else:
                return False

    # @staticmethod
    # def ucwords(text):
    #     uc_text = ''
    #     for id_c, char in enumerate(text):
			# if char in whitespace or not char.isalpha():
				# uc_text += char
			# elif char.isalpha() and (not id_c or text[id_c - 1] in whitespace):
				# uc_text += char.upper()
			# else:
				# uc_text += char
		# return uc_text


class Validator:

    @staticmethod
    def is_null(module, name, value):
        if not value:
            return APP_ERRORS[module][name]

    @staticmethod
    def is_float(number):
        try:
            float(number)
            return True
        except:
            return False


class Slugify:

    @staticmethod
    def slugify(string):
        """
        Make a slug from string
        """

        string = str(string).lower().strip()
        string = Slugify.normalize(string)
        string = re.sub(r'[^\w\s-]', '', string)
        return re.sub(r'[-\s]+', '-', string)

    @staticmethod
    def normalize(string):
        replacements = (
            ("á", "a"),
            ("é", "e"),
            ("í", "i"),
            ("ó", "o"),
            ("ú", "u"),
            ("ñ", "n"),
            ("Á", "a"),
            ("É", "e"),
            ("Í", "i"),
            ("Ó", "o"),
            ("Ú", "u"),
            ("Ñ", "n"),
            ("ü", "u"),
            ("?", ""),
            ("¿", ""),
            ("!", ""),
            ("¡", "")
        )
        for a, b in replacements:
            string = string.replace(a, b)
        return string

# =================================================================================================
#                                          ALIAS
# =================================================================================================
def read_file(filename):
    return FilesHelper.read_file(filename)

def in_html(content):
    return FilesHelper.in_html(content)

def ucwords(text):
	return Sanitizer.ucwords(text)

def slugify(string):
    return Slugify.slugify(string)
