import http.server
import socketserver
import termcolor
from urllib.parse import urlparse, parse_qs
import server_utils as su

PORT = 8084

list_sequences = ['ACCGTGGTGTAACGAAA', 'ATTTGCTGTCTCT', 'CTCTCTCGAGAGAG', 'TACTCGGCCG', 'CGCGTAGGGATGACGTAGC']
list_genes = ['ADA', 'FRAT1', 'FXN', 'RNU6_269P', 'U5']

BASES_INFORMATION = {
    "A": {"link": "https://en.wikipedia.org/wiki/Adenine",
          "formula": "C5H5N5",
          "name": "ADENINE",
          "color": "lightgreen"
    },
    "C": {"link": "https://en.wikipedia.org/wiki/Cytosine",
          "formula": "C4H5N3O",
          "name": "CYTOSINE",
          "color": "yellow"
          },
    "G": {"link": "https://en.wikipedia.org/wiki/Guanine",
          "formula": "C5H5N5O",
          "name": "GUANINE",
          "color": "lightskyblue"
          },
    "T": {"link": "https://en.wikipedia.org/wiki/Thymine",
          "formula": "C5H6N2O2",
          "name": "THYMINE",
          "color": "lightpink"
          }
}

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        termcolor.cprint(self.requestline, 'green')
        termcolor.cprint(self.path, 'blue')

        o = urlparse(self.path)
        path_name = o.path
        arguments = parse_qs(o.query)
        print("Resource requested: ", path_name)
        print("Parameters:", arguments)

        context = {}

        if path_name == "/":
            context['n_sequences'] = len(list_sequences)
            context['list_genes'] = list_genes
            contents = su.read_template_html_file('./html/index.html').render(context=context)
        elif path_name == '/test':
            contents = su.read_template_html_file('./html/test.html').render()
        elif path_name == '/ping':
            contents = su.read_template_html_file('./html/ping.html').render()
        elif path_name == '/get':
            number_sequence = arguments['sequence'][0]
            contents = su.get(list_sequences, number_sequence)
        elif path_name == '/gene':
            gene = arguments['gene'][0]
            contents = su.gene(gene)
        elif path_name == '/operation':
            sequence = arguments['sequence'][0]
            operation = arguments['calculation'][0]
            if operation == 'Info':
                contents = su.info(sequence)
            elif operation == 'Comp':
                contents = su.comp(sequence)
            elif operation == 'Rev':
                contents = su.rev(sequence)
        else:
            contents = su.read_template_html_file('./html/error.html').render()
        self.send_response(200)

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(contents.encode()))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())

        return
Handler = TestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()
