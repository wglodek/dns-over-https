#!/usr/bin/env python
import os
from setuptools import setup
from dns_over_https import __version__ as version


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='dns_over_https',
    version=version,
    description="Python client for Google's Public DNS-over-HTTPS service",
    long_description=read('README.md'),
    keywords="google dns https",
    author='William Glodek',
    author_email='wglodek@breakpoint-labs.com',
    license='MIT',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'License :: OSI Approved :: MIT License',
        'Development Status :: 3 - Alpha',
    ],
    url='https://www.github.com/wglodek/dns-over-https',
    download_url='https://www.github.com/wglodek/dns-over-https/dns_over_https/tarball/0.0.1',  # noqa
    py_modules=['dns_over_https'],
    test_suite='dns_over_https_test',
    install_requires=['requests'],
)
