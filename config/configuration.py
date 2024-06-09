import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configuration for server and application settings
config = {
    # Enable debug mode for development, set to False in production
    'DEBUG': os.getenv('DEBUG', 'true') == 'true',


    # Port on which the server will listen for incoming requests
    # Default: 5000
    'APP_PORT': os.getenv('APP_PORT', '5000'),  


    # Hostname or IP address for the server
    # Default: localhost
    'APP_URL': os.getenv('APP_URL', '127.0.0.1'),  


    # Application basepath for the static files.
    # Default: resources
    'STATIC_FILES_BASEPATH': os.getenv('STATIC_FILES_BASEPATH', 'resources'),


    # Secret key for session management and cryptographic purposes
    # Ensure this is kept confidential and secure
    'SECRET_KEY': os.getenv('SECRET_KEY', 'your_secret_key_here'),  


    # Logging level for the application, controlling the verbosity of log messages
    # Default: INFO
    'LOG_LEVEL': os.getenv('LOG_LEVEL', 'INFO'),  


    # Timezone used by the application to handle date and time-related operations
    # Default: UTC
    'TIMEZONE': os.getenv('TIMEZONE', 'UTC'),  


    # Add more configurations as needed...
}
