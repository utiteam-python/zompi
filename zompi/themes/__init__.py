from .sonzi import Theme as DefaultTheme

ACTIVE_THEME = DefaultTheme()

def use(theme_class):
    global ACTIVE_THEME
    ACTIVE_THEME = theme_class()
  
