#!/usr/bin/env python
#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: 
# Mail: 
# Created Time:  
#############################################


from setuptools import setup, find_packages

setup(
    name = "ai-web",
    version = "0.0.1",
    keywords = ("pip"),
    description = "AI自动生成接口",
    long_description = "这是一个AI自动生成接口的工具，最近会逐步完善",
    license = "MIT Licence",

    author = "HH",
    author_email = "",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = []
)
