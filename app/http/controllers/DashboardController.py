from sproutepy.SprouteApp import SprouteApp 

from app.http.utils.AuthUtil import AuthUtil
from sproutepy.Helper import view, route 

class DashboardController(SprouteApp):
        
    def __init__(self) -> None:
        pass
    
    def index(self, request):
        return view('dashboard', {
            'status': 'success', 
            'message': "Welcome back!",
            'page_title': "Dashboard Page",
        })