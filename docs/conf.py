# -- Project information -----------------------------------------------------

project = 'Odot-App'
copyright = '2024, Victor Rocha'
author = 'Victor Rocha'

# The full version, including alpha/beta/rc tags
release = '0.1.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.intersphinx',
    'sphinx_rtd_theme',
    'myst_parser',
    'sphinxcontrib.mermaid',

]

html_theme = "sphinx_rtd_theme"

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
