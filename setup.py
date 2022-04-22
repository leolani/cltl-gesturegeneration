#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_namespace_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("VERSION", "r", encoding="utf-8") as fh:
    version = fh.read().strip()

setup(
    name="cltl.gesture_generation",
    description="The Leolani module for gesture generation",
    version=version,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/leolani/cltl-gesturegeneration",
    license='MIT License',
    authors={
        "Baez Santamaria": ("Selene Baez Santamaria", "s.baezsantamaria@vu.nl"),
        "Adamik": ("Mark Adamik", "m.adamik@vu.nl")
    },
    package_dir={'': 'src'},
    packages=find_namespace_packages(include=['cltl.*', 'cltl_service.*'], where='src'),
    package_data={'cltl.gesture_generation': [
    ]},
    python_requires='>=3.7',
    install_requires=[
    ],
    extras_require={
        "service": [
            "cltl.combot",
        ]
    },
    setup_requires=['flake8']
)
