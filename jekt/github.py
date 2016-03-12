from getpass import getpass

import keyring
import requests


class GithubError(Exception):
	pass


class Github:
	api_base_url = 'https://api.github.com/'
	keyring_prefix = 'gh-'
	api_version_header = 'application/vnd.github.v3+json'


	def __init__(self):
		self._ssh_urls = {}


	def authenticate(self, username, password=None):
		if password is None:
			password = keyring.get_password('system', self.keyring_prefix + username)
		if password is None:
			password = getpass('password: ')
			keyring.set_password('system', self.keyring_prefix + username, password)

		self._username = username
		self._password = password

	
	def list_repos(self):
		r = self.requests_call(requests.get, self.api_base_url + 'user/repos')

		return [i['name'] for i in r.json()]


	def create_repo(self, name, description=None):
		params = {
				'name'		: name,
				'description'	: description
				}

		r = self.requests_call(requests.post, self.api_base_url + 'user/repos', json=params)

		if r.status_code != 201:
			raise GithubError('error creating repo, [%d] %s'%(r.status_code, r.reason))

		self._ssh_urls[name] = r.json()['ssh_url']


	def delete_repo(self, name):
		r = self.requests_call(requests.delete, self.api_base_url + 'repos/' + self._username + '/' + name)

		if r.status_code != 204:
			raise GithubError('error deleting repo, [%d] %s'%(r.status_code, r.reason))


	def requests_call(self, method, *args, **kwargs):
		kwargs['auth'] = auth=(self._username, self._password)
		headers = {'Accept' : self.api_version_header }
		kwargs['headers'] = headers

		return method(*args, **kwargs)
		

	def get_ssh_url(self, repo_name):
		return self._ssh_urls.get(repo_name, None)

