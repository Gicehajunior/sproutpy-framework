import os
import re
import sys
import glob
from jinja2 import Environment, FileSystemLoader

class TemplatingEngine(Environment, FileSystemLoader):
    def __init__(self, templates_dir=None):
        self.templates_dir = templates_dir
        self.env = Environment(loader=FileSystemLoader(f'{self.templates_dir}'))

    def parse_template(self, template_path):
        file_path = self._locate_file(template_path)
        
        if not file_path or not os.path.isfile(file_path):
            raise FileNotFoundError(f"Template file {file_path} not found.") 
        
        with open(file_path, 'r') as template_file:
            content = template_file.read() 
            
        # Find and replace @ext_loader directives
        content = self._replace_ext_loader(content)
        return content

    def sproute_renderer(self, html_content, response_dump={}): 
        # OPTIONAL: Replace placeholders in HTML with response_dump data
        for key, value in response_dump.items():
            pattern = re.compile(r'\{\{\s*' + re.escape(key) + r'\s*\}\}')
            # Replace placeholders with corresponding values
            html_content = pattern.sub(str(value), html_content)
    
        # Compile the template
        template = self.env.from_string(html_content) 
        
        # Render HTML from the template with the provided data
        html_content = template.render(response_dump)
        
        return html_content

    def _replace_ext_loader(self, content):
        # Regex to match @ext_loader("layout.header") or similar patterns
        pattern = r'@ext_loader\("(.+?)"\)'
        matches = re.findall(pattern, content)

        for match in matches:
            # Convert `.` to `/` and append `.html`
            include_path = match.replace('.', '/') + '.html'
            included_file_path = self._locate_file(include_path)

            if included_file_path:
                with open(included_file_path, 'r') as include_file:
                    include_content = include_file.read()
                
                # Replace the directive with the content of the included file
                content = content.replace(f'@ext_loader("{match}")', include_content)
            else:
                raise FileNotFoundError(f"Included file {include_path} not found.")
        
        return content

    def _locate_file(self, relative_path):
        """
        Locate the file in the templates directory (along its first-level subdirectories),
        supporting both .html and .php extensions.
        """
        # Define possible extensions
        possible_extensions = ['.html', '.php']

        # Iterate over each possible extension to construct search patterns
        for ext in possible_extensions:
            # Add the extension if not already present in relative_path
            search_path = relative_path if relative_path.endswith(ext) else relative_path + ext 
            search_pattern = os.path.join(self.templates_dir, '**', search_path)
            
            # Use glob to find matching files
            matches = glob.glob(search_pattern, recursive=True)

            # Return the first match, if any
            if matches:
                return matches[0]

        # Return None if no match is found
        return None
