
from redcmd.api import Subcommand, subcmd, CommandError


class Client(Subcommand):

	@subcmd
	def test(self, option=None):
		'''Subcommand for testing.

		option: an optional argument'''

		print('this is an example of a subcommand')

