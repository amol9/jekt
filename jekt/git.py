from __future__ import absolute_import
from os import sep

from git import Repo, GitCommandNotFound, Actor
from asq.initiators import query

from .logger import log


class GitError(Exception):
	pass


class Git:
	
	def __init__(self, path):
		self._path 	= path
		self._repo 	= None
		self._remote 	= None


	def init(self):
		try:
			self._repo = Repo.init(path=self._path, mkdir=False)
		except GitCommandNotFound as e:
			log.error(e)
			return False

		return self._repo is not None


	def add(self, paths=None):
		if paths is None:
			paths = ['.']

		index = self._repo.index
		l = index.add(paths)
		index.write()


	def commit(self, message, author_name=None, author_email=None):
		author = None
		if author_name is not None:
			author = Actor(author_name, author_email)

		self._repo.index.commit(message, author=author)


	def get_remote(self):
		if self._repo is not None and self._remote is None:
			self._remote = Remote(self._repo)
		return self._remote

	remote = property(get_remote)

	
class Remote:

	def __init__(self, repo):
		self._repo = repo


	def add(self, name, url):
		self._repo.create_remote(name, url)


	def push(self, name=None):
		remotes = self._repo.remotes

		if len(remotes) == 0:
			raise GitError('no remotes added for repo')

		if name is None:
			return self._repo.remotes[0]
		else:
			q = query(remotes).where(lambda r : r.name == name)
			if q.count == 0:
				raise GitError('no such remote: %s'%name)
			return q[0]

