import json
from urllib.parse import urlparse
from http.server import HTTPServer
from sproutepy.SprouteRequestHandler import SproutRequestHandler
from sproutepy.TemplatingEngine import TemplatingEngine as engine

class SprouteApp:
    def __init__(self):
        self.router = None
        self.database_manager = None
        self.template_engine = None

    def set_router(self, router):
        self.router = router

    def set_database_manager(self, database_manager):
        self.database_manager = database_manager

    def set_template_engine(self, template_engine):
        self.template_engine = template_engine
        
    def strip_protocol(self, url):
        parsed_url = urlparse(url)
        if parsed_url.scheme:
            return url.replace(parsed_url.scheme + "://", "")
        else:
            return url
        
    def start(self, app, host_endpoint='127.0.0.1', port=8000, debug=True):
        host = self.strip_protocol(host_endpoint)
        server_address = (host, port)
        httpd = HTTPServer(server_address, lambda *args, **kwargs: SproutRequestHandler(app, *args, **kwargs))
        print(f'Serving on port {port}')
        httpd.serve_forever()
