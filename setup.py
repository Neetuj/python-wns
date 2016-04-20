from __future__ import absolute_import
from setuptools import setup, find_packages

setup(
    name='python-wns',
    version='0.1',
    description='wns python library',
    long_description=open('README.md', 'r').read(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 2.7',
    ],
    author='Neetu Jain',
    license='BSD License',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'setuptools',
        'eventlet',
        'requests'
    ],
    setup_requires=[],
)
