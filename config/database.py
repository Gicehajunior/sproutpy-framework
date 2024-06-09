import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

database = {
    # MySQL Database Configuration
    'mysql_database': {
        'connection': 'mysql',
        'host': os.getenv('DB_HOST', '127.0.0.1'),            # MySQL server host
        'port': os.getenv('DB_PORT', '3306'),                 # MySQL server port
        'user': os.getenv('DB_USER', 'root'),                 # MySQL username
        'password': os.getenv('DB_PASSWORD', ''),             # MySQL password
        'database': os.getenv('DB_NAME', 'sproutedb'),        # MySQL database name
        'charset': os.getenv('DB_CHARSET', 'utf8mb4'),        # Character set for MySQL
        'pool_size': int(os.getenv('DB_POOL_SIZE', '5')),     # Connection pool size for MySQL
    },
    
    # PostgreSQL Database Configuration
    'postgresql_database': { 
        'connection': 'postgresql',
        'host': os.getenv('DB_HOST', '127.0.0.1'),            # PostgreSQL server host
        'port': os.getenv('DB_PORT', '5432'),                 # PostgreSQL server port
        'user': os.getenv('DB_USER', 'postgres'),             # PostgreSQL username
        'password': os.getenv('DB_PASSWORD', ''),             # PostgreSQL password
        'database': os.getenv('DB_NAME', 'sproutedb'),        # PostgreSQL database name
        'ssl_mode': os.getenv('DB_SSL_MODE', 'prefer'),       # SSL mode for PostgreSQL
        'min_connections': int(os.getenv('DB_MIN_CONNECTIONS', '1')),  # Minimum number of connections for PostgreSQL
        'max_connections': int(os.getenv('DB_MAX_CONNECTIONS', '5')),  # Maximum number of connections for PostgreSQL
    },
    
    # SQLite Database Configuration
    'sqlite_database': {
        'file_path': os.getenv('DB_FILE_PATH', 'db/database.sqlite'),  # Path to SQLite database file
        'timeout': float(os.getenv('DB_TIMEOUT', '5.0')),                      # Timeout for SQLite database operations
    },
    
    # MongoDB Database Configuration
    'mongodb_database': {
        'connection': 'mongodb',
        'host': os.getenv('DB_HOST', '127.0.0.1'),            # MongoDB server host
        'port': os.getenv('DB_PORT', '27017'),                # MongoDB server port
        'username': os.getenv('DB_USER', ''),                 # MongoDB username
        'password': os.getenv('DB_PASSWORD', ''),             # MongoDB password
        'database': os.getenv('DB_NAME', 'sproutedb'),        # MongoDB database name
        'auth_source': os.getenv('DB_AUTH_SOURCE', 'admin'),  # Authentication source for MongoDB
        'ssl': bool(os.getenv('DB_SSL', 'False')),            # Whether SSL/TLS should be used for MongoDB connection
    },
    
    # Add configurations for other database types as needed
    # 'redis_database': {
    #     ...
    # },
    
    # '...': {
    #     ...
    # },
    
    # Add more databases and their configurations here
}
