# setup.py
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
setup(
    author="SAT",
    classifiers=[
        'License :: MIT License',
        'Programming Language :: Python :: 3.9',
    ],
    description="A package to retrieve passwords from the Passwordstate API",
    license="MIT license",
    include_package_data=True,
    name='Passwords',
    packages=['passwords.py'],
    version='0.1.0',
    zip_safe=False,
)
