import create-ticket

def getnetworkdevicecount():


controller='sandboxapicem.cisco.com'

def getTicket():
    # Put the IP address or DNS of your APIC-EM controller in this URL
    url = "https://" + controller + "/api/v1/ticket"

    # The username and password to access the APIC-EM Controller
    payload = {"username":"devnetuser","password":"Cisco123!"}

    # Content type must be included in the header
    header = {"content-type": "application/json"}

    # Perform a POST on the specified url to get the service ticket
    response= requests.post(url,data=json.dumps(payload), headers=header, verify=False)

    # Convert response to JSON format
    r_json=response.json()

    # Parse the JSON to get the service ticket
    ticket = r_json["response"]["serviceTicket"]

    return ticket


def getNetworkDevices(ticket):
    # URL for network device REST API call to get list of devices on the network.
    url = "https://" + controller + "/api/v1/network-device"

    # Include the content type and ticket in the header
    header = {"content-type": "application/json", "X-Auth-Token":ticket}

    # This statement performs a GET on the specified network device url
    response = requests.get(url, headers=header, verify=False)

    # json.dumps serializes the JSON into a string and enables you to
    # Print the response in a 'pretty' format with indentation etc.
    print ("Network Devices = ")
    print (json.dumps(response.json(), indent=4, separators=(',', ': ')))

  # Convert data to JSON format.
    r_json=response.json()

  # Iterate through network device data and print the id and series name of each device
    for i in r_json["response"]:
        print(i["id"] + "   " + i["series"])

# Call the functions
theTicket=getTicket()
getNetworkDevices(theTicket)



