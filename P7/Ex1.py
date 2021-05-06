import http.client
import json

SERVER = "rest.ensembl.org"
ENDPOINT = "/info/ping"
PARAMETERS = "?content-type=application/json"

print("Server: " + SERVER)
print("URL: " + SERVER + ENDPOINT + PARAMETERS)

connection = http.client.HTTPConnection(SERVER)
connection.request("GET", ENDPOINT + PARAMETERS)
response = connection.getresponse()
decoded_answer = response.read().decode()
dict_response = json.loads(decoded_answer)
if dict_response["ping"] == 1:
    print("Response received!:", response.status, response.reason)
    print("PING OK! The database is running!!")
else:
    print("The database is down!")