#!/usr/bin/python
import pymongo, json

# initialize all of my local modules
from modules import *

# initialize the configuration json file
config_file = "./config.json"

# initialize the configuration file!
def get_config():

	try:
		with open(config_file, "r") as read:

			# convert the string of json into a dictionary
			data = json.loads(read.read())

			return data

	except Exception as e:

		print e
		exit()


def main():

	config = get_config()

	# get_token.Get_token(get_config()).new_token()
	# create_repo.Create_repo(get_config())
	# get_repos.Get_repos(get_config())

	


main()





