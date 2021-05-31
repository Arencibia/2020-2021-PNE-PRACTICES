import pathlib
import jinja2
import http.client

def read_html_file(filename):
    return jinja2.Template(pathlib.Path(filename).read_text())