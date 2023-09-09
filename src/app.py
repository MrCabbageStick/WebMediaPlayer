from flask import Flask, render_template, jsonify, redirect
from modules.databaseHandler import DatabaseHandler
from modules.paths import DATABASE

app = Flask(__name__)

database = DatabaseHandler(DATABASE)

@app.route("/")
def homePage():
    return render_template("gallery.html")

@app.route("/movies")
def moviesPage():
    return jsonify(database.getMovies())

@app.route("/addMovie")
def addMoviePage():
    print(database.addMovie("Test", "/test/test/test", None, 10))
    return redirect("/movies")

@app.route("/users")
def usersPage():
    return jsonify(database.getUsers())

@app.route("/addUser")
def addUserPage():
    return jsonify(database.addUser("test", "Testowy", "zaq1@WSX", True))



if __name__ == "__main__":
    database.connect()
    app.run()