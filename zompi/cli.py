import argparse
import os
from pathlib import Path
import zompi
from zompi.page import BasePage

def cmd_version(args):
    print(zompi.getversion())

def cmd_new(args):
    filename = args.file

    template = f'''from zompi.page import BasePage
import zompi.contrib

class Page(BasePage):
    PAGE_TITLE = "{Path(filename).stem}"

    def __init__(self):
        return zompi.contrib.markdown("## Nuova pagina Zompi")

    def __str__(self):
        return BasePage.page(zompi.contrib.DOC, "Markdown")
'''

    with open(filename, "w", encoding="utf-8") as f:
        f.write(template)

    print(f"✔ Creato file: {filename}")

def cmd_convert(args):
    file = Path(args.file)

    if not file.exists():
        print(f"Errore: il file {file} non esiste")
        return

    module_name = file.stem
    module = __import__(module_name)
    page = module.Page()
    html = str(page)

    out = file.with_suffix(".html")
    out.write_text(html, encoding="utf-8")

    print(f"✔ Convertito in HTML: {out}")

def main():
    parser = argparse.ArgumentParser(
        prog="zompi",
        description="CLI ufficiale di Zompi"
    )

    parser.add_argument("-v", "--version", action="store_true",
                        help="Mostra la versione di Zompi")

    sub = parser.add_subparsers()

    # zompi new file.py
    p_new = sub.add_parser("new", help="Crea un file base per una pagina")
    p_new.add_argument("file", help="Nome del file Python da creare")
    p_new.set_defaults(func=cmd_new)

    # zompi convert file.py
    p_convert = sub.add_parser("convert", help="Converte una pagina in HTML")
    p_convert.add_argument("file", help="File Python da convertire")
    p_convert.set_defaults(func=cmd_convert)

    args = parser.parse_args()

    if args.version:
        cmd_version(args)
        return

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()
      
