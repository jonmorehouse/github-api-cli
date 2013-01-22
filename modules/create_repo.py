# this can extend a base class later when I have more time
# import base_request class as parent
from base_request import Base_request

class Create_repo(Base_request):

	def __init__(self, config):

		super(Create_repo, self).__init__(config)
		self.controller()

	def controller(self):

		url = "https://api.github.com/user/repos"

		data = {
		  "name": "TEST",
		  "description": "Test, not a real repo",
		  "homepage": "https://github.com",
		  "private": False,
		  "has_issues": True,
		  "has_wiki": False,
		  "has_downloads": False
		}

		response = self.oauth_post_request(url, data)

		print response







		

