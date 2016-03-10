import ez_setup
ez_setup.use_setuptools()
from setuptools import setup, find_packages

from {{jekt.module_name}}.version import __version__

{% if jekt.setup.redcmd %}
from rc_setup import {{jekt.setup.redcmd_imports}}
{% endif %}

entry_points = {}

{% if jekt.setup.entry_point.console_scripts %}
entry_points['console_scripts'] = ['{{jekt.project_name}}={{jekt.module_name}}main:main']
{% endif %}
{% if jekt.setup.entry_point.gui_scripts %}
import platform
if platform.system() == 'Windows':
	entry_points['gui_scripts'] = ['{{jekt.project_name}}s={{jekt.module_name}}main:main']
{% endif %}

setup(	
	name			= '{{jekt.project_name}}',
	version			= __version__,
	description		= '{{jekt.project_description}}',
	author			= '{{jekt.author}}',
	author_email 		= '{{jekt.email}}',
	url			= 'http://pypi.python.org/pypi/{{jekt.project_name}}/',
	packages		= find_packages(), 
	include_package_data	= True,
	scripts			= [{{jekt.setup.scripts|quoted_list}}],
	entry_points 		= entry_points,
	install_requires	= [{{jekt.setup.install_requires|quoted_list}}],
	classifiers		= [
					{{jekt.setup.classifiers|quoted_list}}	
				]
)

{% if jekt.setup.redcmd %}
setup_autocomp('{{jekt.client}}', '{{jekt.project_name}}', _to_hyphen={{jekt.redcmd.us_to_hyphen}})
{% endif %}

