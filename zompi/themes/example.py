# zompi/themes/default.py

from zompi.contrib import style

class Theme:
    def __init__(self):
        self.THEME_STYLESHEET = style("""
body {
    color: #000;
    background: #fff;
    font-family: sans-serif;
}
""")
      
