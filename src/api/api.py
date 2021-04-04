import flask
from flask import render_template
from flask import request
import file_manager

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route("/api", methods=["GET"])
def index():
    return render_template("home.html")

@app.route("/api/online-positions", methods=["GET"])
def online_positions():
    return file_manager.read()

@app.route("/api/update-positions", methods=["GET", "PUT"])
def update_positions():
    if request.method == "GET":
        return "<p>Specify data within request body.</p>"
    elif request.method == "PUT":
        data = request.get_json()
        return file_manager.write(data)

if __name__ == "__main__":
    app.run()