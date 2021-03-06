# -*- coding: utf-8 -*-
#
# helga documentation build configuration file, created by
# sphinx-quickstart on Mon Dec 22 16:42:46 2014.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os

sys.path.insert(0, os.path.abspath('.'))

import helga

# -- General configuration ------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
]
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

project = helga.__title__
author = helga.__author__
description = helga.__description__
copyright = helga.__copyright__

version = helga.__version__
release = helga.__version__

exclude_patterns = []
show_authors = True
pygments_style = 'sphinx'


# -- Options for HTML output ----------------------------------------------

if os.environ.get('READTHEDOCS', None) != 'True':
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [
        sphinx_rtd_theme.get_html_theme_path(),
    ]
    html_theme_options = {
        'analytics_id': 'UA-57964703-1',
    }
    html_static_path = ['_static']
    htmlhelp_basename = 'helga{0}'.format(release.replace('.', '_'))


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [(
    'index',
    '{0}.tex'.format(project),
    '{0} Documentation'.format(project),
    author,
    'manual',
)]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(
    'index',
    project,
    '{0} Documentation'.format(project),
    [author],
    1,
)]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [(
    'index',
    'helga',
    '{0} Documentation'.format(project),
    author,
    project,
    description,
    'Miscellaneous'),
]
