from sproutepy.SprouteApp import SprouteApp 

from app.http.utils.AuthUtil import AuthUtil
from sproutepy.Helper import view, route 

class AuthController(SprouteApp):
    def __init__(self) -> None:
        self.response = None
    
    def login(self, request):
        return view('auth.login', {
            'status': 'success', 
            'message': 'Please login!',
            'username': 'gicehajunior76@gmail.com', 
            'password': 'gicehajunior76@gmail.com' 
        })

    def signup(self, request):
        return view('auth.signup', {
            'status': 'success', 
            'message': 'Please signup!' 
        })

    def login_user(self, request):
        self.input['username'] = request.get('username')
        self.input['password'] = request.get('password')
        
        return route('dashboard', {
            'status': 'success', 
            'message': self.input
        })

    def signup_user(self, request):
        return route('/login', {
            'status': 'success', 
            'message': 'Logout successfull' 
        })

    def logout(self, request):
        return route('/login', {
            'status': 'success', 
            'message': 'You got booted out. Please login!' 
        })
