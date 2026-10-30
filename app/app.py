import os
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

ROOT = os.path.dirname(os.path.abspath(__file__))
PORT = int(os.environ.get("DATABRICKS_APP_PORT", "8000"))

handler = partial(SimpleHTTPRequestHandler, directory=ROOT)
ThreadingHTTPServer(("0.0.0.0", PORT), handler).serve_forever()
