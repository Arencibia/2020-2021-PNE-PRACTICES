import pathlib
import jinja2
import http.client
import json
from pathlib import Path


def read_template_html_file(filename):
    content = jinja2.Template(pathlib.Path(filename).read_text())
    return content

def get(n, SEQUENCES_LIST):
    sequence = SEQUENCES_LIST[int(n)]
    context = {
        "number": n,
        "sequence": sequence,}
    contents = read_template_html_file("./html/get.html").render(context=context)
    return contents

SERVER = 'rest.ensembl.org'
GOOD_REQUEST = 200
BAD_REQUEST = 400

def list_species(limit=None):
    endpoint = '/info/species'
    argument = '?content-type=application/json'
    url = endpoint + argument

    connection = http.client.HTTPConnection(SERVER)
    connection.request("GET", url)
    response = connection.getresponse()
    status = GOOD_REQUEST
    if response.status == GOOD_REQUEST:
        data = json.loads(response.read().decode("utf-8"))
        try:
            species = data['species']
            context = {
                "total": len(species),
                "species": species[:limit],
                "limit": limit
            }
            contents = read_template_html_file("./html/species.html").render(context=context)
        except KeyError:
            status = BAD_REQUEST
            contents = Path("./html/error.html").read_text()
    else:
        status = BAD_REQUEST
        contents = Path("./html/error.html").read_text()
    return status, contents


def karyotype(specie):
    endpoint = '/info/assembly/'
    argument = f'{specie}?content-type=application/json'
    url = endpoint + argument

    connection = http.client.HTTPConnection(SERVER)
    connection.request("GET", url)
    response = connection.getresponse()
    status = GOOD_REQUEST
    if response.status == GOOD_REQUEST:
        data = json.loads(response.read().decode("utf-8"))
        try:
            karyotype = data['karyotype']

            context = {
                "karyotype": karyotype,
            }
            contents = read_template_html_file("./html/karyotype.html").render(context=context)
        except KeyError:
            status = BAD_REQUEST
            contents = Path("./html/error.html").read_text()
    else:
        status = BAD_REQUEST
        contents = Path("./html/error.html").read_text()
    return status, contents


def chromosome_length(specie, chromo):
    endpoint = '/info/assembly/'
    parameters = f'{specie}?content-type=application/json'
    url = endpoint + parameters

    connection = http.client.HTTPConnection(SERVER)
    connection.request("GET", url)
    response = connection.getresponse()
    status = GOOD_REQUEST
    if response.status == GOOD_REQUEST:
        data = json.loads(response.read().decode("utf-8"))
        try:
            key = data['top_level_region']
            length = 0
            for chromosome in key:
                if chromosome['name'] == chromo:
                    length = chromosome['length']
                    break

            context = {
                "length": length,
            }
            contents = read_template_html_file("./html/chromosomeLength.html").render(context=context)
        except KeyError:
            status = BAD_REQUEST
            contents = Path("./html/error.html").read_text()
    else:
        status = BAD_REQUEST
        contents = Path("./html/error.html").read_text()
    return status, contents





