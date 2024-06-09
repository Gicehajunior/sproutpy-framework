from .Util import Util
from app.models.Auth import Auth as AuthModel

class AuthUtil(Util):
    
    def __init__(self) -> None:
        pass
    
    def getUsers(self):
        return [];