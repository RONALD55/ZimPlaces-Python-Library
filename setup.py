from setuptools import setup, find_packages

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
    version='1.0.6',
    description='A package for wards,districts,cities and provinces in Zimbabwe',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='https://github.com/RONALD55/ZimPlaces-Python-Library',
    author='Ronald Nyasha Kanyepi',
    author_email='kanyepironald@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords=['zimbabwe', 'cities in Zimbabwe', 'districts in Zimbabwe', 'wards in Zimbabwe', 'Provinces in Zimbabwe',
              'Zimbabwe places'],
    packages=find_packages(),
    install_requires=['pandas']
)
