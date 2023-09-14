from flask import Flask, render_template, jsonify, redirect
from modules.config import Config
from modules.databaseHandler import DatabaseHandler
from modules.movieRegistry import MovieRegistry
from modules.paths import DATABASE, CONFIG


app = Flask(__name__)
config = Config(CONFIG)

database = DatabaseHandler(DATABASE)

movieRegistry = MovieRegistry(
    *map(lambda movieDir: movieDir.path, config.movieDirectories),
    allowedExtensions=config.allowedExtensions
)

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
    return jsonify([str(path) for path in movieRegistry.foundFiles])



if __name__ == "__main__":
    database.connect()
    app.run()