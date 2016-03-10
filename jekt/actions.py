

class Component:
	__metaclass__ = ABCMeta

	@abstractmethod
	def create(self):
		pass

	@abstractmethod
	def update(self):
		pass


class BaseComponent(Component):
	template_file = None

	def __init__(self, env, config):
		self._env = env
		self._config = config


	def create(self):
		template = env.get_template(self.template_file)
		file_content = template.render(jekt=self._config)
		
		with(open(self.get_dest_path(), 'w')) as f:
			f.write(file_content)
		

	def get_dest_path(self):
		return joinpath(self._config.project_name, self.template_file)


	def update(self):
		# prompt y/n
		self.create()

