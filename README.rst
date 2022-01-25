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

.. code-block:: python

    from zim_places import *
    import json

    # Get the data as json
    print(get_cities())
    print(get_wards())
    print(get_provinces())
    print(get_districts())

    # Get the data as a list of dictionaries, remember you can customize the list to suit your need
    data = json.loads(get_wards())
    list_of_wards = [{i['Ward'] + ' ' + i['Province_OR_District']} for i in data.values()]
    print(list_of_wards)

    data = json.loads(get_districts())
    list_of_districts = [{i['District'] + ' ' + i['Province']} for i in data.values()]
    print(list_of_districts)

    data = json.loads(get_provinces())
    list_of_provinces = [{i['Province'] + ' ' + i['Capital'] + i['Area(km2)'] + i['Population(2012 census)']} for i in data.values()]
    print(list_of_provinces)

    data = json.loads(get_cities())
    list_of_cities = [{i['City'] + ' ' + i['Province']} for i in data.values()]
    print(list_of_cities)


License
-------

The project is licensed under the MIT license.
