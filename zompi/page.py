# zompi/page.py

import zompi.contrib as c
from zompi.themes import ACTIVE_THEME


class BasePage:
    """
    Classe base per tutte le pagine Zompi.
    Ogni pagina deve definire PAGE_TITLE e implementare __str__().
    """

    PAGE_TITLE = "Untitled"

    @classmethod
    def page(cls, doc, format="Markdown"):
        """
        Combina il titolo della pagina con il contenuto del documento.
        Per ora supportiamo solo Markdown.
        """
        if format == "Markdown":
            return cls._render_markdown(doc)
        else:
            raise ValueError(f"Formato non supportato: {format}")

    @classmethod
    def _render_markdown(cls, doc):
        """
        Rende una pagina Markdown semplice:
        # Titolo
        <contenuto>
        """
        title = f"# {cls.PAGE_TITLE}\n\n"
        content = str(doc)
        stylesheet = str(ACTIVE_THEME.THEME_STYLESHEET)
        return f"{stylesheet}\n\n# {cls.PAGE_TITLE}\n\n{content}"
      
