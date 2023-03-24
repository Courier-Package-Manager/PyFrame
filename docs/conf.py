# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sys
import os

sys.path.insert(0, os.path.abspath('..'))

project = 'pyframe'
copyright = '2023, Joshua Rose'
author = 'Joshua Rose'
release = '0.1.0-prealpha'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.autosectionlabel',
              'sphinx.ext.autosummary',
              'sphinx.ext.coverage',
              'sphinx.ext.doctest',
              'sphinx.ext.duration',
              'sphinx.ext.extlinks',
              'sphinx.ext.githubpages',
              'sphinx.ext.graphviz',
              'sphinx.ext.ifconfig',
              'sphinx.ext.imgconverter',
              'sphinx.ext.inheritance_diagram',
              'sphinx.ext.intersphinx',
              'sphinx.ext.napoleon',
              'sphinx.ext.todo',
              'sphinx.ext.viewcode']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

source_suffix = '.rst'

master_doc = 'index'

todo_include_todos = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_material'
html_static_path = ['_static']
