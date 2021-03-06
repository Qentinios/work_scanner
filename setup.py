from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    # $ pip install work_scanner
    name='work_scanner',
    version='1.3',
    description='A tool that helps with finding interesting job offers',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Adrian Czok',
    author_email='theadrianczok@gmail.com'
)

