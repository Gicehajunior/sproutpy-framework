import os 
import json
import mimetypes
from http import cookies
from urllib.parse import parse_qs
from email.parser import BytesParser
from email.policy import default
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
    
    def parse_multipart_form_data(self, content_type: str, body: bytes):
        """
        Parse multipart/form-data using Python's modern email package.
        Returns a simple dict of key=value and key=file-object.
        """
        if "boundary=" not in content_type:
            raise ValueError("Multipart 'boundary' missing")

        boundary = content_type.split("boundary=")[1]

        header = f"Content-Type: {content_type}\r\n\r\n".encode()
        msg = BytesParser(policy=default).parsebytes(header + body)

        parsed = {}

        for part in msg.iter_parts():
            disposition = part.get("Content-Disposition")
            if not disposition:
                continue

            params = dict(part.get_params(header="content-disposition"))
            name = params.get("name")
            filename = params.get("filename")

            if not name:
                continue

            if filename:  # file upload
                parsed[name] = {
                    "filename": filename,
                    "content_type": part.get_content_type(),
                    "data": part.get_payload(decode=True),
                }
            else:  # text field
                parsed[name] = part.get_payload(decode=True).decode(
                    part.get_content_charset() or "utf-8"
                )

        return parsed

    def parse_request_data(self, content_type):
        parsed_data = {}
        content_length = int(self.headers.get("Content-Length", 0))
        post_data = self.rfile.read(content_length) if content_length > 0 else b""

        # multipart/form-data
        if "multipart/form-data" in content_type:
            try:
                parsed_data = self.parse_multipart_form_data(content_type, post_data)
            except Exception as e:
                self.send_error(400, f"Malformed multipart data: {e}")
                parsed_data = {}
        elif 'application/x-www-form-urlencoded' in content_type:
            content_length = int(self.headers['Content-Length'])
            post_data = post_data.decode('utf-8')
            parsed_data = parse_qs(post_data)
        elif 'text/plain' in content_type:
            content_length = int(self.headers['Content-Length'])
            post_data = post_data.decode('utf-8')
            parsed_data = self._parse_text_plain_data(post_data)
        else:
            self.send_error(415, "Unsupported media type") 
        
        return parsed_data
        
    def serve_static_asset(self, path):
        static_dir = os.getcwd()  # Directory where your static files are stored
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
            response = route_handler(request) # call the controller method bound to this route, & parse the request data.
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
