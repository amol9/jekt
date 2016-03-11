import ez_setup
ez_setup.use_setuptools()

import platform
import sys
from setuptools import setup, find_packages

from rc_setup import setup_autocomp

from jekt.version import __version__


entry_points = {}
entry_points['console_scripts'] = ['jekt=jekt.main:main']

setup(	
	name			= 'jekt',
	version			= __version__,
	description		= 'A command line tool to create and manage python projects.',
	author			= 'Amol Umrale',
	author_email 		= 'babaiscool@gmail.com',
	url			= 'http://pypi.python.org/pypi/jekt/',
	packages		= find_packages(), 
	include_package_data	= True,
	scripts			= ['ez_setup.py', 'rc_setup.py'],
	entry_points 		= entry_points,
	install_requires	= ['redlib>=1.3.0', 'redcmd>=1.1.7', 'enum34', 'GitPython>=1.0.2', 'PyGithub>=1.26.0'],
	classifiers		= [
					'Development Status :: 4 - Beta',
					'Environment :: Console',
					'License :: OSI Approved :: MIT License',
					'Natural Language :: English',
					'Operating System :: POSIX :: Linux',
					'Programming Language :: Python :: 2.7',
					'Programming Language :: Python :: 3.4'
				]
)


setup_autocomp('jekt.client', 'jekt', _to_hyphen=True)

