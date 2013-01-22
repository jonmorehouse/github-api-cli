from base_request import Base_request


class Delete_repo(Base_request):

	def __init__(self, config):

		super(Delete_repo, self).__init__(config)
		self.controller()


	def delete_repo(self, repository_name):

		url = "https://api.github.com/repos/%s/%s" % (self.config['username'], repository_name)

		data = {

			

		}




	def get_help(self, config):pass


		# get the help in case there is an invalid option given


	def parse_data(self, input):pass


		# will parse the data will return the data







