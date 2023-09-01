from flask import Flask, render_template, jsonify, redirect
from modules.databaseHandler import DatabaseHandler
from modules.paths import DATABASE

app = Flask(__name__)

database = DatabaseHandler(DATABASE)

@app.route("/")
def homePage():
    return render_template("gallery.html")

@app.route("/users")
def usersPage():
    return jsonify(database.getUsers())

@app.route("/addUser")
def addUserPage():
    print(database.addUser("osk", "Ośk", "lubie_jelenie", True))
    return redirect("/users")



if __name__ == "__main__":
    database.connect()
    app.run()