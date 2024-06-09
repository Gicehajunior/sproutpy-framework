"""
********************************************************************************************************

                                SPROUTEPY FRAMEWORK

This is the main entry point for the SPROUTEPY Framework.

[ Framework Overview ]
SPROUTEPY is a lightweight Python framework designed for simplicity,
flexibility, and ease of use. It follows the MVC (Model-View-Controller)
architectural pattern and includes various components for
routing, database interaction, and template rendering.

[ File Structure ]
- app/http/controllers/      : Contains controllers for handling requests.
- app/models/                : Houses model classes for interacting with the database.
- resources/views/           : Stores template files for rendering views.
- config/                    : Configuration files for database connections, Core framework files and classes, etc.
- public/                    : Publicly & privately accessible assets (stylesheets, images, storage, etc.). 

[ Getting Started ]
To start using SPROUTEPY, make sure to configure your database
settings in the 'config/database.py' file. Create controllers
in the 'controllers/' directory and corresponding views in
the 'views/' directory. The public assets can be placed in
the 'public/' directory.

[ Documentation ]
For detailed documentation and examples, visit the official
SPROUTEPY documentation at https://sproutepyframework.com/docs.

[ Version Information ]
SPROUTEPY Framework v1.0.0

[ Author ]
[Your Name] - https://github.com/Gicehajunior

[ License ]
This framework is released under the MIT License. See the LICENSE file for details.
https://github.com/Gicehajunior/sproutepy-framework/blob/main/LICENSE

********************************************************************************************************
""" 
from sproutepy.SprouteApp import SprouteApp 
from sproutepy.DatabaseManager import DatabaseManager as DB
from sproutepy.SprouteRequest import SproutRequest 
from routes.pathway import router
from config.database import database
from config.configuration import config 

def simulate_request(method, path, body=None):
    request = SproutRequest(method, path, body)
    response = request.handle_request(router)
    print(response)

# Entry point
if __name__ == '__main__':  
    # Initialize the application
    app = SprouteApp()
    
    # Setup database connection
    db_manager = DB(database['mysql_database'])
    db_manager.connect()
    app.set_database_manager(db_manager)
    
    # Setup routing  
    app.set_router(router) 
    
    # Start the server
    app.start(app, host_endpoint=config['APP_URL'], port=int(config['APP_PORT']), debug=config['DEBUG'])


