from setuptools import setup

setup(
    name = 'normalizer',
    version = '0.1.0',
    author = 'Silas Hayes',
    author_email = 'silasjhayes@gmail.com',
    packages = ['normalizer'],
    url = 'https://github.com/silashayes/booklover',
    description = 'A package for normalizing’,
    long_description = open('README.txt').read(),
    install_requires = [
        'numpy']
)