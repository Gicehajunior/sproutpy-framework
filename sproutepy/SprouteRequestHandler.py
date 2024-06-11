import os
import cgi
import json
import mimetypes
from http import cookies
from config.configuration import config 
from http.server import BaseHTTPRequestHandler
from sproutepy.SprouteRequest import SproutRequest 
from urllib.parse import parse_qs, urlparse, urljoin 

class SproutRequestHandler(BaseHTTPRequestHandler):
    def __init__(self, app, *args, **kwargs):
        self.app = app
        self.session = {}
        super().__init__(*args, **kwargs)
    
    def do_GET(self):
        parsed_path = urlparse(self.path)
        if not self.route_request(parsed_path.path, 'GET'):
            self.serve_static_asset(parsed_path.path)
    
    def do_POST(self):
        content_type = self.headers['Content-Type']  
        form_data = self.parse_request_data(content_type) 
        parsed_path = urlparse(self.path)  
        request = SproutRequest('POST', parsed_path.path, form_data)
        response = request.handle_request(self.server.app.router)
        self._handle_response(response)
        
    def parse_request_data(self, content_type):
        parsed_data = {}
        if 'multipart/form-data' in content_type:
            form_data = cgi.FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={'REQUEST_METHOD': 'POST'},
                keep_blank_values=True
            )
            for key in form_data.keys():
                parsed_data[key] = form_data.getvalue(key)
        elif 'application/x-www-form-urlencoded' in content_type:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            parsed_data = parse_qs(post_data)
        elif 'text/plain' in content_type:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            parsed_data = self._parse_text_plain_data(post_data)
        else:
            self.send_error(415, "Unsupported media type") 
        
        return parsed_data
        
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
    
    def route_request(self, path, method, request={}):
        route_handler = self.server.app.router.routes.get(method, {}).get(path)
        if route_handler:
            response = route_handler(request)
            self._send_response(response)
            return True
        return False
    
    def _handle_response(self, response): 
        if isinstance(response, dict):   
            if response['status'] == 302: 
                self.send_response(302)
                self.send_header('Location', response['headers']['Location']) 
                self.end_headers() 
                
        else:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(response.encode('utf-8'))

    def _send_response(self, response):
        if isinstance(response, dict):   
            if response['status'] == 302: 
                self.send_response(302)
                self.send_header('Location', response['headers']['Location']) 
                self.end_headers() 
            
        else:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(response.encode('utf-8'))
    
    def setup(self):
        super().setup()
        self.server.app = self.app
