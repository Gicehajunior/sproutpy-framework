import os
import mimetypes
from http.server import BaseHTTPRequestHandler
from sproutepy.SprouteRequest import SproutRequest 
from urllib.parse import parse_qs, urlparse 
from cgi import FieldStorage 

class SproutRequestHandler(BaseHTTPRequestHandler):
    def __init__(self, app, *args, **kwargs):
        self.app = app
        super().__init__(*args, **kwargs)
    
    def do_GET(self):
        parsed_path = urlparse(self.path)
        if not self.route_request(parsed_path.path, 'GET'):
            self.serve_static_asset(parsed_path.path)
    
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        parsed_path = urlparse(self.path)
        form_data = parse_qs(post_data)
        if not self.route_request(parsed_path.path, 'POST'):
            self.send_error(404, "File not found")

    def serve_static_asset(self, path):
        static_dir = ''  # Directory where your static files are stored
        file_path = os.path.join(static_dir, path.lstrip('/'))

        if os.path.isfile(file_path):
            self.send_response(200)
            mime_type, _ = mimetypes.guess_type(file_path)
            self.send_header('Content-type', mime_type)
            self.end_headers()

            with open(file_path, 'rb') as file:
                self.wfile.write(file.read())
        else:
            self.send_error(404, "File " + f"{path}" + " not found")
    
    def route_request(self, path, method):
        route_handler = self.server.app.router.routes.get(method, {}).get(path)
        if route_handler:
            response = route_handler(None)
            self._send_response(response)
            return True
        return False
    
    def _send_response(self, response):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(response.encode('utf-8'))

    def setup(self):
        super().setup()
        self.server.app = self.app
