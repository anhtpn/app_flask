from flask import Flask, render_template
from flask_restful import Api
from connect import config
from routes.routes import initialize_routes


app = Flask(__name__)
api = Api(app)
config()
initialize_routes(api)

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/movie")
def movie():
    user_details = {
        'name': 'John',
        'email': 'john@doe.com'
    }
    return render_template("movie.html", user=user_details)


if __name__ == "__main__":
    # app.run(debug=True)
    app.run()