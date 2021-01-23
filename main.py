from flask import Flask, render_template
from flask_restful import Api
from connect import config
from routes.routes import initialize_routes


app = Flask(__name__)
api = Api(app)
config()
initialize_routes(api)


if __name__ == "__main__":
    app.run(debug=True)