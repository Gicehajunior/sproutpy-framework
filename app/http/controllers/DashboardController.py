from sproutepy.SprouteApp import SprouteApp 

from app.http.utils.AuthUtil import AuthUtil as authutil
from app.models.Auth import Auth as auth
from sproutepy.Helper import view, route, arr_mutate 

class DashboardController(SprouteApp):
        
    def __init__(self) -> None:
        pass
    
    def index(self, request):
        return view('dashboard', {
            'status': 'success', 
            'message': "Welcome back!",
            'parser': auth.dataload(),
            'auth_session': [('a', 1), ('b', 2), ('c', 3)]
        })