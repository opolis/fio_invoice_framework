#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import (
    find_packages,
    setup,
)

setup(
    name='fio_invoice_framework',
    version='0.0.1',
    description="""FIO Invoice Framework""",
    author='Opolis',
    author_email='support@opolis.co',
    url='https://github.com/opolis/fio_invoice_framework',
    include_package_data=True,
    install_requires=[
        "Django==3.1.14",
    ],
    python_requires='>=3.6,<4',
    license="MIT",
    zip_safe=False,
    keywords='fio',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
