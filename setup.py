#!/usr/bin/env python
""" Package setup/installation and metadata for lambdata
"""

import setuptools

REQUIRED = [
    "numpy",
    "pandas",
    "sklearn"
]

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name="lambdata-carlosgutier",
    version="0.0.7",
    author="carlos-gutier",
    description="A collection of Data Science helper functions",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/carlos-gutier/lambdata",
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    install_requires=REQUIRED,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
