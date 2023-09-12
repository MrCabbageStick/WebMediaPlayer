from flask import Flask, render_template, jsonify, redirect
from modules.databaseHandler import DatabaseHandler
from modules.movieRegistry import MovieRegistry
from modules.paths import DATABASE, CONFIG
import json


with open(CONFIG) as configFile:
    config = json.load(configFile)

app = Flask(__name__)

database = DatabaseHandler(DATABASE)
movieRegistry = MovieRegistry(*[movieDir["path"] for movieDir in config["movie_directories"]], allowedExtensions=config["allowed_extensions"])

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

@app.route("/findMovies")
def findMoviesPage():
    movieRegistry.findMovies()
    return jsonify([path.__str__() for path in movieRegistry.foundFiles])



if __name__ == "__main__":
    database.connect()
    app.run()