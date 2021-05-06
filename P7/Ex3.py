import http.client
import json


def print_colored(message, data, color):
    from termcolor import cprint, colored
    print(colored(message, color), end="")
    print(data)


DICT_GENES = {
    "FRAT1": "ENSG00000165879",
    "ADA": "ENSG00000196839",
    "FXN": "ENSG00000165060",
    "RNU6_269P": "ENSG00000212379",
    "MIR633": "ENSG00000207552",
    "TTTY4C": "ENSG00000228296",
    "RBMY2YP": "ENSG00000227633",
    "FGFR3": "ENSG00000068078",
    "KDR": "ENSG00000128052",
    "ANK2": "ENSG00000145362"
}

SERVER = "rest.ensembl.org"
ENDPOINT = "/sequence/id/"
ID = DICT_GENES["MIR633"]
PARAMETERS = "?content-type=application/json"

print("Server: " + SERVER)
print("URL: " + SERVER + ENDPOINT + PARAMETERS)

connection = http.client.HTTPConnection(SERVER)
connection.request("GET", ENDPOINT + ID + PARAMETERS)
response = connection.getresponse()
print("Response received!:", response.status, response.reason)
if response.status == 200:
    response = json.loads(response.read().decode())
    print_colored("Gene: ",ID, "yellow")
    print_colored("Description: ", response["desc"], "yellow")
    print_colored("Bases: ", response["seq"], "yellow")
elif response.status == 404:
    print("Check if the ENDPOINT was correctly written!!!")