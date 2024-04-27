# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'argus documents'
copyright = '2024, Ashish'
author = 'Ashish'
release = '1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

html_theme_options = {
   
    'logo_only': True,
    # 'display_version': True,
    'prev_next_buttons_location': 'bottom',
    # 'style_external_links': False,
    # 'vcs_pageview_mode': '',
    'style_nav_header_background': 'white',
    # Toc options
    'collapse_navigation': True,
    # 'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}


language = 'English'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_logo = 'images/arguslogo.png'
html_static_path = ['_static']
