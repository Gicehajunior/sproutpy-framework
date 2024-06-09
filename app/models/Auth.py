import os
from sproutepy.DatabaseManager import DatabaseManager as DB

class Auth(DB):
    
    table = 'users'
    
    def __init__(self) -> None:
        pass
    
    