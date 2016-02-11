#!/usr/bin/env python

from setuptools import setup

setup(
    name='lsib-django',
    version='1.0.0',
    install_requires=[],
    author='Patrick Dufour',
    author_email='pjdufour.dev@gmail.com',
    license='BSD License',
    url='https://github.com/wfp-ose/lsib-django',
    keywords='python gis wfp lsib',
    description='LSIB Django, Version 1.x',
    long_description=open('README.rst').read(),
    download_url="https://github.com/wfp-ose/lsib-django/zipball/master",
    packages=[
        "lsibdjango",
        "lsibdjango.tests"],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
