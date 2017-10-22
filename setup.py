from os import path
from setuptools import setup, find_packages

HERE = path.abspath(path.dirname(__file__))
VERS = '0.1a'
DESC = 'Script to create local backups from airtable databases'

with open(path.join(HERE, 'README.rst'), 'r') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='airtable_local_backup',
    version=VERS,

    description=DESC,
    long_description=LONG_DESCRIPTION,

    url='https://github.com/rickh94/airtable_local_backup',
    author='Rick Henry',
    author_email='fredericmhenry@gmail.com',

    license='MIT',
    python_requires='>=3',

    packages=find_packages(),

    install_requires=[
        'requests',
        'airtable-python-wrapper',
        'boto3',
    ],
    tests_require=['pytest', 'pytest-cov'],
    setup_requires=['pytest-runner'],

)
