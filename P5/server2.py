import http.server
import socketserver
import termcolor
import pathlib
import jinja2

def read_html_file(filename):
    contents = pathlib.Path(filename).read_text()
    return contents

def read_template_html_file(filename):
    contents = jinja2.Template(pathlib.Path(filename).read_text())
    return contents
# Define the Server's port
PORT = 8080

BASES_INFORMATION = {
    "A":{"link": "https://es.wikipedia.org/wiki/Adenina" ,
        "formula": "C5H5N5",
        "name": "ADENINE",
        "color": "green"
    },
    "C": {"link": "https://es.wikipedia.org/wiki/Citosina",
          "formula": "C4H5N30",
          "name": "CYTOSINE",
          "color": "yellow"
    },
    "G" : {"link":"https://es.wikipedia.org/wiki/Guanina",
           "formula":"C5N5H5",
           "name": "GUANINE",
           "color":"lightskyblue"
    },
    "T": {"link": "https://es.wikipedia.org/wiki/Timina",
          "formula":"C5H6N202",
          "name": "THYMINE",
          "color":"lightpink"
    }

}


# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):


    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')
        termcolor.cprint(self.path, 'blue')


        # IN this simple server version:
        # We are NOT processing the client's request
        # It is a happy server: It always returns a message saying
        # that everything is ok

        if self.path == "/":
            contents = read_html_file("./html/index.html")
        elif "/info/" in self.path:
            base = self.path.split("/")[-1]
            context = BASES_INFORMATION[base]
            context["letter"] = base
            contents = read_template_html_file("./html/info/general.html").render(base_information= context)

        elif self.path.endswith(".html"):
            try:
                contents = read_html_file("./html" + self.path)
            except FileNotFoundError:
                contents = read_html_file("./html/error.html")
        else:
            contents = read_html_file("./html/error.html")
        # Message to send back to the clinet


        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html') # Si no ponemos html saldrá texto!!
        self.send_header('Content-Length', len(contents.encode()))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())

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
