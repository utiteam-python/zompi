from zompi.page import BasePage
import zompi.contrib

class Page(BasePage):
    PAGE_TITLE = "Esempio"

    def __init__(self):
        return zompi.contrib.markdown('''## Esempio 
Esempio Markdown''')

    def __str__(self):
        return BasePage.page(zompi.contrib.DOC, 'Markdown')
      
