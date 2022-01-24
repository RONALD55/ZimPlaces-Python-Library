from setuptools import setup, find_packages
from glob import glob

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Intended Audience :: Developers',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='zim_places',
    version='1.1.9',
    description='A package for wards,districts,cities and provinces in Zimbabwe',
    long_description=open('README.rst').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='https://github.com/RONALD55/ZimPlaces-Python-Library',
    author='Ronald Nyasha Kanyepi',
    author_email='kanyepironald@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords=['zimbabwe', 'cities in Zimbabwe', 'districts in Zimbabwe', 'wards in Zimbabwe', 'Provinces in Zimbabwe',
              'Zimbabwe zim_places'],
    packages=find_packages(),
    install_requires=['pandas'],
    include_package_data=True,
    package_data={'zim_places': glob('components/*.csv')}

)
