# Zompi

_Un generatore di documentazione Python-centrico con temi modulari_

---

## Installa Zompi

Per installare Zompi, digita nel terminale:

```bash
pip install zompi
```

---

## Crea una pagina di documentazione

Crea un file, ad esempio `lorem_ipsum.py` e scrivici:

```python
from zompi.page import BasePage
import zompi.contrib

class Page(BasePage):
    PAGE_TITLE = "Lorem Ipsum"

    def __init__(self):
        return zompi.contrib.markdown('''## Testo 
Lorem ipsum dolor sit amet, consectetur adipisci elit, sed eiusmod tempor incidunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur. Quis aute iure reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint obcaecat cupiditat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.''')

    def __str__(self):
        return BasePage.page(zompi.contrib.DOC, 'Markdown')
```

Se ti stai chiedendo cosa significa `zompi.contrib.DOC`, quella constante si riferisce a quel documento, se si usa un'altra variabile, userá un altro documento.

---

## Aggiungere un tema

Per aggiungere un tema, all'inizio di una pagina inserisci inserisci:

```python
from modulotema import Theme
from zompi.theme import use
```

e nella classe della pagina (preferibilmente in `__init__()`) inserite:

```python
use(Theme)
```

Ricorda che di defalut Zompi usa il tema Sonzi (ovvero `zompi.theme.sonzi`)

---

## Altri pacchetti

Guarda anche [DeWeb](https://pypi.org/project/DeWeb) e [utiilityes](https://pypi.org/project/utiilityes)

---

## Versioni nuove, supportate e EOL

| Versione | Stato | Note |
|----------|-------|------|
| 0.1.0 | Nuova | — |
