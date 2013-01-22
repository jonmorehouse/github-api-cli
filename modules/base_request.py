# this class is useful for sending requests to github's api 
# will be responsible for maintaining the configuration for this app 
# as well as making individual requests

import urllib2
import urllib
import json

class Base_request(object):


	def __init__(self, config):

		self.config = config


	def encode_user(self):
			
		# Authorization: token OAUTH-TOKEN" https://api.github.com
		return "Basic " + (self.config['username'] + ":" + self.config['password']).encode("base64").rstrip()


	# this is responsible for taking in data and sending it if necessary and then returning the basic request
	def basic_request(self, url):

		request = urllib2.Request(url)

		request.add_header("Authorization", self.encode_user())

		response = urllib2.urlopen(request).read()		
		return json.loads(response)[0]

	def basic_post_request(self, url, data):

		headers = {

			"Authorization": self.encode_user(),
			"Accept": "application/json"
		}

		# generate the request and grab response
		request = urllib2.Request(url, json.dumps(data), headers)

		response = urllib2.urlopen(request).read()

		# return the dictionary that is returned in json
		return json.loads(response)


	def oauth_post_request(self, url, data):

		headers = {

			"Content-type" : "application/json",
			"Authorization" : "token %s" % self.config['token'],
		}


		request = urllib2.Request(url, json.dumps(data), headers)

		try:

			response = urllib2.urlopen(request).read()
			return response

		except Exception, e:	
			print e
		# response = urllib2.urlopen(request).read()

		# print response



	def oauth_get_request(self, url, data):pass




