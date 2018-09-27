from setuptools import setup, find_packages

setup(
    name = 'ccsexampleapi2',
    version = '1.0.0',
    description = 'A very simple Python API service using Flask',
    packages = ['ccsexampleapi2'],    
    install_requires = ['flask', 'psutil'],
)