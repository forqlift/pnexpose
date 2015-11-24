#!/usr/bin/env python
import codecs
from setuptools import setup, find_packages


def read_files(*filenames):
    """
    Output the contents of one or more files to a single concatenated string.
    """
    output = []
    for filename in filenames:
        f = codecs.open(filename, encoding='utf-8')
        try:
            output.append(f.read())
        finally:
            f.close()
    return '\n\n'.join(output)


setup(
    name='pnexpose',
    version='bf99897',
    description='Github forq of pnexpose with a build so that it can be setup.py-ed, forked from github.com/devious1/pnexpose',
    long_description=read_files('README.md',),
    author='divious1',
    author_email='forq@lift.this',
    url='https://github.com/forqlift/pnexpose/',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
)
