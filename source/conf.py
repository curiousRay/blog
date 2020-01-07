# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import sphinx_rtd_theme


# -- Project information -----------------------------------------------------

project = "Ray's sky"
copyright = '2019, curiousRay. Content licensed under CC BY 3.0'
author = 'curiousRay'

# The full version, including alpha/beta/rc tags
release = '0.1'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = [
    'sphinx_rtd_theme',
    'sphinx.ext.mathjax',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = ['style.css']
# html_javascript_files = ['https://www.googletagmanager.com/gtag/js?id=UA-148061851-1', 'ga.js']


def setup(app):
    # app.add_javascript('https://www.googletagmanager.com/gtag/js?id=UA-148061851-1')
    app.add_javascript('ga.js')

# https://github.com/readthedocs/sphinx_rtd_theme/issues/477

# add custom css files

html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'analytics_id': '',
    'canonical_url': '',
    'logo_only': False,
    'display_version': False,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    #'style_nav_header_background': '#2980B9',
    # Toc options
    'collapse_navigation': False,
    'navigation_depth': 4,
}

mathjax_path = 'https://cdn.bootcss.com/mathjax/2.7.6/MathJax.js?config=TeX-AMS-MML_HTMLorMML'

# code highlight
pygments_style = 'trac'

html_title = 'Ray\'s sky'

html_favicon = 'favicon.ico'
