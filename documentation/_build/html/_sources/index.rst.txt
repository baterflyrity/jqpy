.. JQpy documentation master file, created by
   sphinx-quickstart on Sat Dec  2 21:43:54 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to JQpy's documentation!
================================

`JQpy <https://pypi.org/project/jqpy/>`_ is Python binding for `JQ <https://jqlang.github.io/jq/>`_ (JSON processing language) that simply works on any platform (even Windows) and does not require compilation.


Quick example:

.. code:: ipython

	>>> from jqpy import jq
	>>> jq('.results[] | {age, city}', {
			"timestamp": 1234567890,
			"report": "Age Report",
			"results": [
				{ "name": "John", "age": 43, "city": "TownA" },
				{ "name": "Joe",  "age": 10, "city": "TownB" }
			]
		})
	[{'age': 43, 'city': 'TownA'}, {'age': 10, 'city': 'TownB'}]


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   tutorial
   jqpy



