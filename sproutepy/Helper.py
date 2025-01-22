import os
import re
import sys
import json 
from config.configuration import config 
from sproutepy.TemplatingEngine import TemplatingEngine
from sproutepy.Router import Router as router  

def view(route, response_dump={}): 
    # Define the base directory for resources
    base_dir = config['STATIC_FILES_BASEPATH']

    # Define the file path
    file_path =  f"{route}" 
    
    # Load HTML content from the file 
    parser = TemplatingEngine(base_dir)
    html_content = parser.parse_template(file_path) 
    html_content = parser.sproute_renderer(html_content, response_dump)
    
    return html_content

def route(route, response_dump={}): 
    return {
        'status': 302,
        'headers': {
            'Location': route
        },
        'body': response_dump
    }
    
def arr_mutate(dictionary):
    return list(dictionary.items())