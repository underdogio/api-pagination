api-pagination
==============

.. image:: https://travis-ci.org/underdogio/api-pagination.png?branch=master
   :target: https://travis-ci.org/underdogio/api-pagination
   :alt: Build Status

Pagination calculator designed for APIs

When building an API, out of bound pages should be treated with empty result sets. The existing solutions were not doing this. We have designed ``api-pagination`` to handle these edge cases from the perspective of an API.

Getting Started
---------------
Install the module with: ``pip install api_pagination``

.. code:: python

    # Load in dependencies
    from api_pagination import Paginator

    # Generate a paginator and get info about a page
    paginator = Paginator(total=100, items_per_page=10)
    page_info = paginator.get_page_info(page=2)
    {
        'overall': {
            'first_page': 1,
            'last_page': 10,
            'pages': 10,
            'total': 100
        },
        'page': {
            'current_page': 2,
            'next_page': 3,
            'previous_page': 1
        }
    }

    # Use a classmethod to get info in one fell swoop
    page_info = Paginator.page_info(page=1, total=100, items_per_page=10)
    {
        'overall': {
            'first_page': 1,
            'last_page': 10,
            'pages': 10,
            'total': 100
        },
        'page': {
            'current_page': 1,
            'next_page': 2,
            'previous_page': None
        }
    }

    # Handle out of bounds properly
    page_info = Paginator.page_info(page=20, total=100, items_per_page=10)
    {
        'overall': {
            'first_page': 1,
            'last_page': 10,
            'pages': 10,
            'total': 100
        },
        'page': {
            'current_page': 20,
            'next_page': None,
            'previous_page': 10
        }
    }


Documentation
-------------
We expose the ``Paginator`` class via our package ``api_pagination``

Paginator(total, items_per_page)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Class for calculating pagination info about items

- total ``int`` - Overall amount of items present
- items_per_page ``int`` - How many items to include on each page

paginator.get_page_info(page)
"""""""""""""""""""""""""""""
Gather information about a given page

- page ``int`` - Human based index for a page

  - For example, page 1 will be for items 1-10 (where ``items_per_page=10``)

**Returns:**

- ret_val ``dict`` - Container for information about overall information and page specific information

  - overall ``dict`` - Container for overall information

    - first_page ``int`` - Human based index for first page

      - For example, with ``total=20`` and ``items_per_page=10``, we have ``first_page=1``

    - last_page ``int`` - Human based index for last page

      - For example, with ``total=25`` and ``items_per_page=10``, we have ``last_page=3`` (includes items 21-25)

    - pages ``int`` - Amount of pages overall

      - For example, with ``total=25`` and ``items_per_page=10``, we have ``pages=3``

    - total ``int`` - Amount of items overall

  - page ``dict`` - Container for page specific information

    - current_page ``int`` - Human based index of requested page
    - next_page ``int|None`` - If there is another page after this one, ``next_page`` will be that page's human based index

      - For example, with ``total=25``, ``items_per_page=10``, and ``page=2``, we have ``next_page=3`` (includes items 21-25)
      - When on the last page (e.g. `total=25`, ``items_per_page=10``, ``page=3``) ``next_page`` will be ``None``
      - If we are under bounds (e.g. ``page=-1``), then ``next_page`` will be the first page (``page=1``)

    - previous_page ``int|None`` - If there is another page before this one, ``previous_page`` will be that page's human based index

      - For example, with ``total=25``, ``items_per_page=10``, and ``page=2``, we have ``previous_page=1`` (includes items 1-10)
      - When on the first page (e.g. ``total=25``, ``items_per_page=10``, ``page=1``) then ``previous_page`` will be ``None``
      - If we are over bounds (e.g. ``total=25``, ``items_per_page=10``, ``page=4``), then ``previous_page`` will be the last page (``page=3``)

Paginator.page_info(page, \*args, \*\*kwargs)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Helper function to get page info without calling multiple actions

- page ``int`` - Page to pass through to ``paginator.get_page_info``
- \*args - Ordered arguments to pass through to ``Paginator`` constructor
- \*\*kwargs - Keyword based arguments to pass through to ``Paginator`` constructor

**Returns:**

Returns same format as ``paginator.get_page_info``

**Example:**

.. code:: python

    page_info = Paginator.page_info(page=1, total=100, items_per_page=10)
    # Same as
    # paginator = Paginator(total=100, items_per_page=10)
    # page_info = paginator.get_page_info(page=1)


Contributing
------------
In lieu of a formal styleguide, take care to maintain the existing coding style. Add unit tests for any new or changed functionality. Test via ``./test.sh``.

License
-------
Copyright (c) 2015 Underdog.io

Licensed under the MIT license.
