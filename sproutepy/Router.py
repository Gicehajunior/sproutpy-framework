import os
import json
import sys
from config.configuration import config 

class Router:
    def __init__(self):
        self.routes = {
            'GET': {},
            'POST': {},
            'PUT': {},
            'DELETE': {}
        }

    def get(self, path, handler):
        self._add_route(path, handler, methods=['GET'])

    def post(self, path, handler):
        self._add_route(path, handler, methods=['POST'])

    def put(self, path, handler):
        self._add_route(path, handler, methods=['PUT'])

    def delete(self, path, handler):
        self._add_route(path, handler, methods=['DELETE'])

    def _add_route(self, path, handler, methods):  
        for method in methods:
            if method in self.routes:
                self.routes[method][path] = handler

    def add_route(self, path, controller, action, methods=['GET']):
        def route_handler(request):
            controller_instance = controller()
            method = getattr(controller_instance, action)
            return method(request)
        
        for method in methods:
            if method in self.routes:
                self.routes[method][path] = route_handler

    def serve_static_asset(self, path):
        # Define the directory where static assets are located
        static_dir = ''
        asset_path = os.path.join(static_dir, path.lstrip('/'))
        if os.path.isfile(asset_path): 
            with open(asset_path, 'rb', encoding="utf-8") as file: 
                return file.read()
        else:
            return '404 Error: ' + f'{asset_path}' + ' could not be found'

    def route_request(self, path, method, body=None): 
        # Check if the route exists for the given method and path
        route_handler = self.routes.get(method, {}).get(path)
        if route_handler:
            return route_handler(body)
        
        # If not found in dynamic routes, try serving static assets
        if method == 'GET':
            return self.serve_static_asset(path)
        
        # If no route matches, return 404 Not Found
        return '404 Route Error: ' + f'{route_handler}' + ' could not be found!'
    