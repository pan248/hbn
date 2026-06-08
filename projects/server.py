import os
import http.server
import socketserver

PORT = int(os.environ.get("DEPLOY_RUN_PORT", "5000"))
DIRECTORY = os.path.dirname(os.path.abspath(__file__))


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)


with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
    print("Serving at port", PORT, "directory", DIRECTORY, flush=True)
    httpd.serve_forever()
