import os
import re
import sys
import json 
from config.configuration import config 
from sproutepy.TemplatingEngine import TemplatingEngine
from sproutepy.Router import Router as router 
from jinja2 import Environment, FileSystemLoader

def view(route, response_dump={}): 
    # Define the base directory for resources
    base_dir = config['STATIC_FILES_BASEPATH']

    # Define the file path
    file_path =  f"{route}.html" 
    
    # Load HTML content from the file 
    parser = TemplatingEngine(base_dir)
    html_content = parser.parse_template(file_path) 

    # OPTIONAL: Replace placeholders in HTML with response_dump data
    for key, value in response_dump.items():
        pattern = re.compile(r'\{\{\s*' + re.escape(key) + r'\s*\}\}')
        # Replace placeholders with corresponding values
        html_content = pattern.sub(str(value), html_content)
    
    env = Environment(loader=FileSystemLoader(f'{base_dir}'))
    # Compile the template
    template = env.from_string(html_content) 
    # Render HTML from the template with the provided data
    html_content = template.render(response_dump) 
    
    return html_content

def route(route, response_dump={}): 
    return {
        'status': 302,
        'headers': {
            'Location': route
        },
        'body': response_dump
    }