# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import sphinx_rtd_theme
# import caktus_theme
# import sphinx_bernard_theme
# import stanford_theme
from recommonmark.parser import CommonMarkParser
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
# html_theme_path = [caktus_theme.get_theme_dir()]
# html_theme_path = [sphinx_bernard_theme.get_html_theme_path()]
# html_sidebars = caktus_theme.default_sidebars()
# html_theme_path = [stanford_theme.get_html_theme_path()]
# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
source_parsers = {
    '.md': CommonMarkParser,
        }
source_suffix = ['.rst', '.md']

# -- Project information -----------------------------------------------------

project = 'notebook'
copyright = '2021, sean'
author = 'sean'

# The full version, including alpha/beta/rc tags
release = '1.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
        'recommonmark',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
# html_theme = 'classic'
# html_theme = 'caktus'
# html_theme = 'insegel'
# html_theme = 'sphinx_bernard_theme'
# html_theme = 'stanford_theme'
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
