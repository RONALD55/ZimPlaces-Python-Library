============
Zim-Places
============
.. image:: https://img.shields.io/pypi/v/country_list.svg
        :target: https://pypi.org/project/zim-places

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
        :target: https://github.com/RONALD55/ZimPlaces-Python-Library

Features
--------

- This is a python package that allows you to search for cities, provinces, and districts in Zimbabwe.Zimbabwe is split into eight provinces and two cities that are designated as provincial capitals.
  Districts are organized into 59 provinces.Wards are organized into 1,200 districts.Visit the project homepage for further information on how to use the package.



Installation
------------

To can install the zim_places open shell or terminal and run::

    pip install zim-places

Usage
-----

Get all wards:

.. code-block:: python

    from zim_places import wards
    print(wards.get_wards())

Get all districts:

.. code-block:: python

    from zim_places import districts
    print(districts.get_districts())

Get all cities:

.. code-block:: python

    from zim_places import cities
    print(cities.get_cities())

Get all provinces:

.. code-block:: python

    from zim_places import provinces
    print(provinces.get_provinces())

License
-------

The project is licensed under the MIT license.
