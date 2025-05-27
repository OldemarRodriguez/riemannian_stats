import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

# -- Project Information --

project = 'RiemannianStats'
author = 'Oldemar Rodríguez Rojas, Jennifer Lobo Vásquez'
release = '1.0.0'

# -- General Configuration --

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',
]

templates_path = ['_templates']
exclude_patterns = []

# -- HTML Output Options --

html_theme = 'furo'

html_title = "Riemannian STATS"

html_theme_options = {
    "light_logo": "images/logo.jpg",
    "sidebar_hide_name": False,
    "navigation_with_keys": True,
}


html_static_path = ['_static']

html_css_files = [
    'css/base.css',   # común
    'css/light.css',  # modo claro
    'css/dark.css'    # modo oscuro
]

html_js_files = [
    'js/theme-switch.js'
]

# -- Autodoc Settings --

autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'show-inheritance': True,
}

# -- Napoleon Settings (for Google/NumPy docstrings) --

napoleon_google_docstring = True
napoleon_numpy_docstring = True

# -- Extension --

todo_include_todos = True
source_suffix = '.rst'