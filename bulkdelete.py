# 	IMPORTANT NOTE: This is meant as an example only. This is a code I personally wrote for my environment and is not Okta supported. 
#	Modify the code to meet your needs and complete testing before running in a production environment 
# 	Okta REST API: https://developer.okta.com/docs/reference/postman-collections/
# 	Okta REST API Guide: https://developer.okta.com/code/rest/
# 	Lanugage: Python3


import requests
import json

# Okta url examples: https://yoursubdomain.okta.com
okta_url = 'enter okta url'
users_api = okta_url + '/api/v1/users'

# Create API Key, following the Create Okta API TOKEN example from: https://help.okta.com/en/prod/Content/Topics/Security/API.htm
API_TOKEN = "Enter API Key"


# Filter for users to be deleted, based on your own needs: https://developer.okta.com/docs/reference/api/users/#list-users-with-a-filter
# Limit can be removed, but when testing, I strongly encourage it to prevent mass deletion of users
# The below example returns all users in a staged environment and limits the list to 1 user (do not increase without testing)
querystring = users_api + '?filter=status eq "STAGED" & limit=1'


headers = {
    'Accept': "application/json",
    'Content-Type': "application/json",
    'Authorization': "SSWS " + API_TOKEN,
    }

response = requests.request("GET", querystring, headers=headers)

json_data = json.loads(response.text)

# Print and stop is added as a stop gap, to make sure users other than those you're expected to be deleted are not included
# During testing, do not remove stop until you have verified that only the users you want to be deleted are included and printed
print (json_data)
stop


# Loops  through and prints the email for each user in the User List before deactivating and deleting 
for r in json_data:
	print (r['profile']['email'])
	userid = str(r['id'])

	url = users_api + "/" + userid
	response = requests.request("DELETE", url, headers=headers)


	url = users_api + "/" + userid
	response = requests.request("DELETE", url, headers=headers)


