import os
from app.models.Model import Model

class Auth(Model):
    
    table = 'users'
    
    def __init__(self) -> None:
        pass
    
    def dataload() -> None:
        return {
            'page_title': "Dashboard Page",
        }