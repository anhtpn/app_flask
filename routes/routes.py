from controller.user_api import LoginApi
def initialize_routes(api):
    api.add_resource(LoginApi, "/api/user")