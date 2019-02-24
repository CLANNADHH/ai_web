#!/usr/bin/env python
# -*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: 
# Mail: 
# Created Time:  
#############################################


from setuptools import setup, find_packages

setup(
    name="ai_web",
    author="clannadhh",
    maintainer="clannadhh",
    version="0.0.2",
    keywords=("pip"),
    description="AI自动生成接口",
    long_description="一个ai算法接口生成模块，详见github https://github.com/CLANNADHH/ai_web",
    url='https://github.com/CLANNADHH/ai_web',
    license="MIT Licence",
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ],
    install_requires=[
        'klein',
        'numpy',
    ]

)
