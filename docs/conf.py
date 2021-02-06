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

project = 'Oltranz documentation'
copyright = '2018-2021, Oltranz Ltd. All rights reserved'
author = 'Oltranz Ltd.'
version = "1.0.0"
release = '1.0.0'

# The full version, including alpha/beta/rc tags


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx_rtd_theme",
    "sphinx_copybutton"
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_theme_options = {
    'logo_only' : True,
    'navigation_depth': 2,
}
html_css_files = [
    'https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css',
    'css/default.css',
]

html_js_files = [
    'js/requests.js',
]

html_favicon = '_static/images/favicon.png'
html_logo = '_static/images/logo-full.png' 
vcs_pageview_mode = 'edit'
html_last_updated_fmt = '%b %d, %Y at %H:%M:%S %Z'
html_show_sphinx = False
pygments_style = 'colorful'

html_context = {
    'display_github': True,
    'github_user': 'OLTRANZ',
    'github_repo': 'publc-documentation',
    'github_version': 'master',
    'conf_py_path': '/docs/',
}

