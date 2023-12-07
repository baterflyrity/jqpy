# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

import os
import sys

sys.path.insert(0, '..')

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'JQpy'
copyright = '2023, baterflyrity@yandex.ru'
author = 'baterflyrity@yandex.ru'

version = '1.0.0'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
	'sphinx.ext.autodoc',
	'sphinx.ext.viewcode',
	'sphinx.ext.todo',
	'sphinx.ext.graphviz',
	'sphinx.ext.inheritance_diagram',
	"sphinx_immaterial",
	'myst_parser',
	'sphinx.ext.githubpages',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_immaterial'
html_static_path = ['_static']

# -- Options for todo extension ----------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/todo.html#configuration

todo_include_todos = True

# Other
sphinx_immaterial_generate_extra_admonitions = True
inheritance_graph_attrs = dict(rankdir="TB", size='""')
html_theme_options = {
	"font"                   : False,
	"icon"                   : {
		"repo": "fontawesome/brands/github",
		"edit": "material/file-edit-outline",
	},
	"site_url"               : "https://baterflyrity.github.io/jqpy/",
	"repo_url"               : "https://github.com/baterflyrity/jqpy/",
	"repo_name"              : "JQpy",
	"globaltoc_collapse"     : True,
	"features"               : [
		"navigation.expand",
		'navigation.instant',
		"navigation.sections",
		"navigation.top",
		"search.highlight",
		"search.share",
		"toc.follow",
		"toc.sticky",
		"content.tabs.link",
		"announce.dismiss",
	],
	"palette"                : [
		{
			"media"  : "(prefers-color-scheme: light)",
			"scheme" : "default",
			"primary": "teal",
			"accent" : "orange",
			"toggle" : {
				"icon": "material/lightbulb-outline",
				"name": "Switch to dark mode",
			},
		},
		{
			"media"  : "(prefers-color-scheme: dark)",
			"scheme" : "slate",
			"primary": "teal",
			"accent" : "orange",
			"toggle" : {
				"icon": "material/lightbulb",
				"name": "Switch to light mode",
			},
		},
	],
	"toc_title_is_page_title": True,
	"social"                 : [
		{
			"icon": "fontawesome/brands/github",
			"link": "https://github.com/baterflyrity/jqpy/",
			"name": "Sources on github.com",
		},
		{
			"icon": "fontawesome/brands/python",
			"link": "https://pypi.org/project/jqpy/",
			'name': 'Python package'
		},
	],
	'version_dropdown'       : True,
	"version_info"           : [
		{
			"version": "https://pypi.org/project/jqpy",
			"title"  : "Get Python package",
			"aliases": [],
		},
		{
			"version": "https://github.com/baterflyrity/jqpy",
			"title"  : "Get sources",
			"aliases": [],
		},
	],
}
