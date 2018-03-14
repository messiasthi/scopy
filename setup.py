#! /usr/bin/env python
from setuptools import setup, find_packages

setup(
	name="Super Copy Paste",
	version="1.0",
	description='A sample Python project',  # Required
	url='https://github.com/messiasthi/scopy',
	author='Thiago Messias',
	author_email='messiasthi@gmail.com',
	packages=find_packages(),
	entry_points={
		'console_scripts': [
			"scopy=scopy:main"
		]
	}
)
