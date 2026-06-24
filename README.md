# Zompi

[![PyPI Version](https://img.shields.io/pypi/v/zompi)](https://pypi.org/project/zompi/)
[![PyPI Downloads](https://img.shields.io/pypi/dm/zompi.svg)](https://pypi.org/project/zompi/)
[![License](https://img.shields.io/pypi/l/zompi)](https://github.com/utiteam-python/zompi/blob/main/LICENSE)
[![GitHub Repo](https://img.shields.io/badge/GitHub-utiteam--python%2Fzompi-blue?logo=github)](https://github.com/utiteam-python/zompi)

_Un generatore di documentazione Python-centrico con temi modulari_

---

## Installa Zompi

Per installare Zompi, digita nel terminale:

```bash
pip install zompi
```

E controlla che sia installato:

```bash
zompi -v
```

Se dá output, allora hai installato correttamente Zompi, altrimenti prova `python -m zompi.cli` o reinstalla Zompi.

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

Se non vuoi copiare questo file esempio, digita nel terminale `zompi new nomefile.py`, che creerá per te un file vuoto.

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

## Convertire in HTML

Per convertire in HTML, digita nel terminale:

```bash
zompi convert nomefile.py
```

Convertirá in HTML velocemente il file.

---

## Altri pacchetti

Guarda anche [DeWeb](https://pypi.org/project/DeWeb) e [utiilityes](https://pypi.org/project/utiilityes)

---

## Versioni nuove, supportate e EOL

| Versione | Stato | Note |
|----------|-------|------|
| 0.1.x | supportata | — |

