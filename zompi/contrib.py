# zompi/contrib.py

import markdown as md


class Document:
    """
    Rappresenta un documento generato da una pagina Zompi.
    Contiene contenuto già renderizzato (Markdown o HTML).
    """
    def __init__(self, content=""):
        self.content = content

    def set(self, content):
        self.content = content

    def append(self, content):
        self.content += "\n" + content

    def __str__(self):
        return self.content


# Documento principale della pagina corrente
DOC = Document()


def markdown(text: str) -> str:
    """
    Converte Markdown in HTML.
    """
    return md.markdown(text)

class Style:
    def __init__(self, css: str):
        self.css = css

    def __str__(self):
        return self.css


def style(css: str) -> Style:
    return Style(css)
    
