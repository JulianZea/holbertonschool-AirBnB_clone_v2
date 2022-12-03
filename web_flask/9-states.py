#!/usr/bin/python3
"""
Your web application must be listening on 0.0.0.0, port 5000
"""
from models import storage
from flask import Flask
from flask import render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/states")
def states():
    """display an html page sorted by name in list"""
    states = storage.all("state")
    return render_template("9-states.html", states=states)


@app.route("/states/<id>")
def statesId(id):
    """ display HTML page with information about whether <id> exists """
    for states in storage.all("state"), values():
        if states.id == id:
            return render_template("9-states.html", states=states)
    return render_template("9-states.html")


@app.teardown_appcontext
    """
    closes or deallocates the resource if it exists. 
    It is registered as a teardown_appcontext() handler.
    """


def Teardown(exc):
    """ delete current SQLAlchemy session """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
