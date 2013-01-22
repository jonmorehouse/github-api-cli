from base_request import Base_request
import urllib2
import urllib
import base64


class Get_token(Base_request):


	def __init__(self, config):

		super(Get_token, self).__init__(config)

		self.data = {

			"add_scopes": ["public_repo", "repo", "delete_repo"],
			"note" : "Github API CLI Tool"
		}


	def new_token(self):

		# 
		response = self.basic_post_request("https://api.github.com/authorizations", self.data)


		print response['id']
		print response['token']


	
	def update_token(self, id):

		url = "https://api.github.com/authorizations/%s" % id

		response = self.basic_post_request(url, self.data)

		print response['token']




