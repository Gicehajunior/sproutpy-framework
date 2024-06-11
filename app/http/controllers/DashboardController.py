from sproutepy.SprouteApp import SprouteApp 

from app.http.utils.AuthUtil import AuthUtil
from sproutepy.Helper import view, route 

class DashboardController(SprouteApp):
        
    def __init__(self) -> None:
        pass
    
    def index(self, request):
        return view('views.dashboard', {
            'status': 'success', 
            'message': "Welcome back!"
        })