from unittest import TestCase, main as ut_main, SkipTest
from shutil import rmtree
from os.path import exists, join as joinpath
from os import mkdir
import sys

from jekt.git import Git
from jekt.logger import log


run_git_tests = True


def gitskip(test_func):
	def test_new(self):
		if run_git_tests:
			test_func(self)
		else:
			raise SkipTest('.git repo already present in current dir')
	return test_new


class TestGit(TestCase):

	@classmethod
	def setUpClass(cls):
		if exists('.git'):
			ch = raw_input('there is a .git dir in current directory,'
					'it may be the root of a valid git repo, do you want to continue? [y/n]: ').strip()
			if ch != 'y':
				global run_git_tests
				run_git_tests = False


	def tearDown(self):
		if run_git_tests:
			if exists('.git'):
				rmtree('.git')


	@gitskip
	def test_init(self):
		path = '.'
		git = Git(path)

		success = git.init()
		self.assertTrue(success)
		self.assertTrue(exists('.git'))


	@gitskip
	def test_init_fail(self):
		non_exst_path = 'non_exst'
		git = Git(non_exst_path)

		success = git.init()
		self.assertFalse(success)
		self.assertFalse(exists('.git'))
		self.assertFalse(exists(non_exst_path))


	@gitskip
	def test_init_add_commit(self):
		path = 'testrepo'
		git = Git(path)
		mkdir(path)

		git.init()
		with open(joinpath(path, 'test.txt'), 'w'):
			pass

		git.add(['test.txt'])
		git.commit('test commit')
		

		
if __name__ == '__main__':
	ut_main()

