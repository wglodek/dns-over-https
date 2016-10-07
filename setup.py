#!/usr/bin/env python
from setuptools import setup
from dns_over_https import __version__ as version

setup(
    name='dns_over_https',
    version=version,
    description="Python client for Google's Public DNS-over-HTTPS service",
    author='William Glodek',
    author_email='wglodek@breakpoint-labs.com',
    license='MIT',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    url='https://www.github.com/wglodek/dns-over-https',
    py_modules=['dns_over_https'],
    test_suite='dns_over_https_test',
    install_requires=['requests'],
)
