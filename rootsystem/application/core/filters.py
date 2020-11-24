# -*- coding: utf-8 -*-


class Filter:

    @staticmethod
    def sanitize_html_tags(string):
        return string.replace("<", "&lt;").replace(">", "&gt;")

    @staticmethod
    def sanitize_quotes(string):
        return string.replace("'", "&#39;").replace('"', "&#34;")

    @staticmethod
    def sanitize_string(string):
        string = string.replace("&", "&amp;")
        string = Filter.sanitize_html_tags(string)
        string = Filter.sanitize_quotes(string)
        string = string.replace("#", "&#35;")
        string = string.replace("?", "&#63;")
        string = string.replace("¿", "&#191;")
        string = Filter.normalize(string)
        return string

    @staticmethod
    def normalize(string):
        replacements = (
            ("á", "&#225;"),
            ("é", "&#233;"),
            ("í", "&#237;"),
            ("ó", "&#243;"),
            ("ú", "&#250;"),
            ("Á", "&#193;"),
            ("É", "&#201;"),
            ("Í", "&#205;"),
            ("Ó", "&#211;"),
            ("Ú", "&#218;"),
            ("ü", "&#252;"),
            ("Ü", "&#220;"),
            ("Ñ", "&#209"),
            ("ñ", "&#241"),
        )
        for a, b in replacements:
            string = string.replace(a, b)
        return string

    @staticmethod
    def sanitize_int(value):
        try:
            value = int(value)
        except:
            value = 0
        return value
