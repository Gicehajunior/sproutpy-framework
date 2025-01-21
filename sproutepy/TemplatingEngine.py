import os
import re
import sys
import glob

class TemplatingEngine:
    def __init__(self, templates_dir=None):
        self.templates_dir = templates_dir

    def parse_template(self, template_path):
        file_path = self._locate_file(template_path)
        
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"Template file {file_path} not found.")

        with open(file_path, 'r') as template_file:
            content = template_file.read() 
            
        # Find and replace @ext_loader directives
        content = self._replace_ext_loader(content)
        return content

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
        Locate the file in the templates directory (Along its first-level subdirectories).
        """
        search_pattern = os.path.join(self.templates_dir, '**', relative_path)
        # Use glob to find matching files
        matches = glob.glob(search_pattern, recursive=True)

        # Return the first match, if any
        return matches[0] if matches else None
