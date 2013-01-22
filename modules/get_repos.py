from base_request import Base_request

import urllib2
import base64


class Get_repos(Base_request):

	def __init__(self, config):

		super(Get_repos, self).__init__(config)
		self.controller()


	def controller(self):


		print self.basic_request("https://api.github.com/authorizations")



		# url = "https://api.github.com/authorizations"
		# request = urllib2.Request(url)
		# request.add_header("Authorization", self.encode_user())

		# # 
		# print urllib2.urlopen(request).read()


		# $ curl -H "Authorization: token OAUTH-TOKEN" https://api.github.com

		
