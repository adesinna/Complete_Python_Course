import requests  # it is used for data collection

response = requests.get(url='http://api.open-notify.org/iss-now.json')  # another attributed called parameters, the rule is
																		# specified by the API.

print(response)  # it will return the success message of 200

# 1XX : hold on
# 2XX : success
# 3XX : forbidden, or you are not allowed
# 4XX: Client side error
# 5XX : Server side error

print(response.status_code)  # sends the status code

response.raise_for_status()  # tells the client the error

data = response.json()
print(data)

print(data['iss_position'])





