# RestApiPythonAssignment1
This assignment is to get the company name for the given mac address using python requests, sys module.

User need to pass mac address cmd line parameter.

Usage:
python pythonFileName.py MACaddress

Ex : python getCompanyName.py 43:28:36:ff:ef:57

Description:
1. This python file collects the mac address as command line argument from the user. it will perform the validation if mac address argument is passed or not.

2. It will store all input varibles for REST API GET request. required headers and query parameters are collected.

3. Performs REST API calls for the given url using API token authenticaiton.

4. The json response is validated for https errors.

5. The json response is parsed and required dictionary key is fetched to display the company name for the given mac address.
