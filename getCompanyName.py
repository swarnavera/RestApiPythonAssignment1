import sys
import requests
from requests.exceptions import HTTPError

'''
Collect MAC address from command line arguments
'''
numOfArgs = len(sys.argv)
# verify the command line argument passed to the program
if numOfArgs==2:
    macAddr = sys.argv[1]
    print("Entered MAC address by the user: ", macAddr)
else:
    print("\n Please rerun the program and provide the MAC Address as command line argument.\n For Ex: python pythonfilename.py MACaddress")
    # exits from program if argument is not provided
    sys.exit(0)

'''
Input variables for REST API access
'''
apiUrl = 'https://api.macaddress.io/v1'
# secured authentication token
apiKey = 'at_kwvQkd0YqYdzEeBOe1N9SUduQQD7L'
api_headers = {'X-Authentication-Token': apiKey}
# parameters in dict format which will be parsed down and added to the base url.
queryParams = {'output': 'json', 'search': macAddr}

'''
Calling the rest api endpoint with parameters and get response. 
prints the company name for the given MAC address.
'''
try:
    response = requests.get(url = apiUrl, params = queryParams, headers = api_headers)
    # check for empty or invalid json response object which servers may return.
    response.raise_for_status()
    jsonResponse = response.json()
    print(jsonResponse)
    print("\nCompany name associated with the given MAC address is : ",jsonResponse["vendorDetails"]["companyName"])
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')