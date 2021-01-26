from flask import Flask, render_template, redirect, url_for, request, session
from flask_restful import Api
from connect import config
from routes.routes import initialize_routes

from my_code.Process import RecommendMovie

from read_file import get_user_id


app = Flask(__name__)
api = Api(app)
config()
initialize_routes(api)


@app.route("/")
def home():
    return render_template("login.html")


@app.route("/recommend")
def recommend():
    movies = []

    if 'user' in session:
        user = session['user']
        print(user)
        movies = RecommendMovie(user)
    return render_template("recommend.html", movies=movies, length=len(movies))


@app.route("/", methods=['POST'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')
    # print(email)
    session["user"] = username
    return redirect(url_for('movie'))


@app.route("/movie")
def movie():
    

    if 'user' in session:
        user = session['user']
        movies = get_user_id(user)

    return render_template("user.html", movies=movies, length=len(movies))


if __name__ == "__main__":
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
    app.run(debug=True)
    # app.run()
