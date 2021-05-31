import pathlib
import jinja2

def read_html_file(filename):
    return jinja2.Template(pathlib.Path(filename).read_text())