import http.server
import socketserver
import termcolor
from urllib.parse import urlparse, parse_qs
import utils
from pathlib import Path


PORT = 9090
ENDPOINTS = ["/listSpecies",
             "/karyotype",
             "/chromosomeLength",
             "/"]


class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')
        termcolor.cprint(self.path, "blue")

        url = urlparse(self.path)
        endpoint = url.path
        argument = parse_qs(url.query)
        print("Endpoint: ", endpoint)
        print("Argument: ", argument)

        GOOD_REQUEST = 200
        BAD_REQUEST = 400

        contents = ""
        status = BAD_REQUEST

        if endpoint in ENDPOINTS:
            if endpoint == "/":
                status = GOOD_REQUEST
                contents = Path("./html/index.html").read_text()
            elif endpoint == "/listSpecies":
                if len(argument) == 0:
                    status, contents = utils.list_species()
                elif len(argument) == 1:
                    try:
                        limit = int(argument['limit'][0])
                        status, contents = utils.list_species(limit)
                        print(contents)
                    except (KeyError, ValueError):
                        contents = Path("./html/error.html").read_text()
                        print(contents)
                else:
                    contents = Path("./html/error.html").read_text()
                    print(contents)
            elif endpoint == "/karyotype":
                if len(argument) == 1:
                    try:
                        specie = argument['specie'][0]
                        status, contents = utils.karyotype(specie)
                        print(contents)
                    except (KeyError, ValueError):
                        contents = Path("./html/error.html").read_text()
                        print(contents)
                else:
                    contents = Path("./html/error.html").read_text()
                    print(contents)
            elif endpoint == "/chromosomeLength":
                if len(argument) == 2:
                    try:
                        specie = argument['specie'][0]
                        chromo = argument['chromo'][0]
                        status, contents = utils.chromosome_length(specie, chromo)
                        print(contents)
                    except (KeyError, ValueError):
                        contents = Path("./html/error.html").read_text()
                        print(contents)
                else:
                    contents = Path("./html/error.html").read_text()
                    print(contents)



        self.send_response(status)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', str(len(contents.encode())))
        self.end_headers()
        self.wfile.write(contents.encode())

handler = TestHandler
with socketserver.TCPServer(("", PORT), handler) as httpd:
    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()