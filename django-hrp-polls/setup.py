import os
from setuptools import setup

with open (os.path.join (os.path.dirname (__file__),
                         'README.md'),
           'rt') as readme:
    README = readme.read ()

# allow setup.py to be run from any path
os.chdir (
    os.path.normpath (
        os.path.join (os.path.abspath (__file__),
                      os.pardir ) ) )

setup (
    name='django-hrp-polls',
    version='0.1',
    packages=['polls'],
    include_package_data=True,
    license='BSD License',  # example license
    description='A simple Django app to conduct Web-based polls.',
    long_description=README,
    url='http://www.example.com/',
    author='Your Name',
    author_email='yourname@example.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: Creative Commons', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
