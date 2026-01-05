# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'BGWarcompany'
copyright = '2025, Helene'
author = 'Helene'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
# Source - https://stackoverflow.com/a
# Posted by Michael Altfield, modified by community. See post 'Timeline' for change history
# Retrieved 2026-01-04, License - CC BY-SA 4.0

html_context = {
  'display_github': True,
  'github_user': 'buskill',
  'github_repo': 'buskill-app',
  'github_version': 'master/docs/',
}


# -- Options for EPUB output
epub_show_urls = 'footnote'
