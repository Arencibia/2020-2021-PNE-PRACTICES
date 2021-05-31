import http.server
import socketserver
import termcolor
import utils
from urllib.parse import urlparse, parse_qs
import pathlib
import json
import jinja2

# Define the Server's port
PORT = 5002

# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        o =urlparse(self.path)
        path_name= o.path
        arguments=parse_qs(o.query)
        print("Resource requested", path_name)
        print("Parameters:", arguments)

        try:
            if path_name== '/':
                contents = utils.read_html_file('html/index.html').render()
            elif path_name=='/listSpecies':
                contents=
            elif path_name == '/karyotype':
                contents=
            elif path_name == '/chromosomeLength':
        except KeyError:
            contents = utils.read_html_file('html/error.html').render()
            print(contents)


        # Generating the response message

        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', str(len(contents.encode())))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()
