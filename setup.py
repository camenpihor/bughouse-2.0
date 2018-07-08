#!/usr/bin/env python2
from setuptools import find_packages, setup


def get_version():
    with open('VERSION') as f:
        return f.read()


setup(
    name="the_bughouse",
    version=get_version(),
    url="https://github.com/camenpihor/bughouse-2.0",
    author="Camen Piho",
    author_email="camenpihor@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=open("requirements.in").readlines(),
    tests_require=open("requirements.testing.in").readlines(),
    description="Repository hosting the code for thebughouse.io",
    long_description=open("README.md").read(),
)
