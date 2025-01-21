# ==============================================================================
# FILE: pathway.py
# ==============================================================================
#
# DESCRIPTION:
# This file defines the router for the SproutPy Framework, responsible for
# mapping HTTP requests to specific controller actions.
#
# MODULES:
# - Router: The main router class responsible for defining routes and mapping
#   them to controller actions.
#
# USAGE:
# 1. Import the required controllers:
#    - AuthController: Handles authentication-related routes.
#    - DashboardController: Handles routes related to dashboard functionalities.
#
# 2. Create an instance of the Router class:
#    router = Router()
#
# 3. Define routes using the router's methods, such as `get`, `post`, `put`, `delete`:
#    Examples:
#    - router.get('/', AuthController().login)
#    - router.post('/login', AuthController().login_user)
#    - router.get('/dashboard', DashboardController().index)
#
# 4. Optionally, additional middleware or route handlers can be added to the router.
#
# NOTES:
# - The Router class is responsible for dispatching requests to the appropriate
#   controller actions based on the requested route.
#
# - Each route is associated with a specific HTTP method and controller action.
#
# - Middleware can be added to perform pre-processing or post-processing tasks
#   on requests before or after they reach the controller actions.
#
# - The Router class plays a central role in defining the application's URL structure
#   and handling incoming requests, making it a critical component of the framework.
#
# EXAMPLE USAGE:
# =============================================================================
# from sproutepy.Router import Router
# from app.http.authentication.AuthController import AuthController
# from app.http.controllers.DashboardController import DashboardController
#
# router = Router()
#
# # Define routes
# router.get('/', AuthController().login)
# router.post('/login', AuthController().login_user)
# router.get('/dashboard', DashboardController().index) 
#
# # Additional routes can be added as needed.
# =============================================================================
#
# AUTHOR: Giceha Junior
# DATE CREATED: 1st June 2024
# VERSION: 1.0.0
# ==============================================================================
import sys
from sproutepy.Router import Router
from app.http.authentication.AuthController import AuthController
from app.http.controllers.DashboardController import DashboardController 
router = Router() 

router.get('/', AuthController().login)
router.get('/dashboard', DashboardController().index) 
router.get('/login', AuthController().login)
router.get('/register', AuthController().signup)
router.post('/login', AuthController().login_user)
router.post('/register', AuthController().signup_user)
router.get('/logout', AuthController().logout)


