import os
import re
import json 
from config.configuration import config 
from sproutepy.Router import Router as router 
from jinja2 import Environment, FileSystemLoader

def view(route, response_dump={}):
    # Extract the resource type and file name from the template_name
    resource_type, file_name = route.split('.')
    
    # Define the base directory for resources
    base_dir = config['STATIC_FILES_BASEPATH']
    
    # Define the directory path based on the resource type
    if resource_type == 'auth':
        directory = os.path.join(base_dir, 'auth')
    elif resource_type == 'views':
        directory = os.path.join(base_dir, 'views')
    elif resource_type == 'layouts':
        directory = os.path.join(base_dir, 'layouts')
    else:
        raise ValueError(f"Invalid resource type: {resource_type}")

    # Define the file path
    file_path = os.path.join(os.getcwd(), directory, f"{file_name}.html")

    # Load HTML content from the file
    with open(file_path, 'r', encoding="utf-8") as file:
        html_content = file.read()

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