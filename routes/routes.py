from controller.user_api import LoginApi, UserId
from controller.run_model_api import ModelApi
def initialize_routes(api):
    api.add_resource(LoginApi, "/api/user")
    api.add_resource(UserId, "/api/user/<user_id>")
    api.add_resource(ModelApi, "/api/model/<user_id>")
