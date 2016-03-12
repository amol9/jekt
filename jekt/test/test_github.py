from unittest import TestCase, main as ut_main

from jekt.github import Github


class TestGithub(TestCase):

	def test_list_repos(self):
		github = Github()
		github.authenticate('amol9')

		some_exp_repos = ['mayloop', 'wallp', 'redcmd', 'fbstats']
		repos = github.list_repos()

		for r in some_exp_repos:
			self.assertIn(r, repos)


	def test_create_repo(self):
		github = Github()
		github.authenticate('amol9')

		repo_name = 'testrepo'
		github.create_repo(repo_name, 'this is test repo created via github api')
		self.assertIsNotNone(github._ssh_urls.get(repo_name, None))


	def test_delete_repo(self):
		github = Github()
		github.authenticate('amol9')

		repo_name = 'testrepo'
		github.delete_repo(repo_name)
		repos = github.list_repos()
		self.assertNotIn(repo_name, repos)


if __name__ == '__main__':
	ut_main()

