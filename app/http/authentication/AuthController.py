from app.http.utils.AuthUtil import AuthUtil
from sproutepy.Helper import view, route, resource 

class AuthController:
    def __init__(self) -> None:
        self.response = None
    
    def login(self, request):
        return view('auth.login', {
            'status': 'success', 
            'username': 'gicehajunior76@gmail.com', 
            'password': 'gicehajunior76@gmail.com' 
        })

    def signup(self, request):
        return 'AuthController: signup'

    def login_user(self, request):
        return 'AuthController: login user'

    def signup_user(self, request):
        return 'AuthController: signup_user'

    def logout(self, request):
        return 'AuthController: logout'
