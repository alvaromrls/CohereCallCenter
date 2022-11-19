from flask import Flask, request
from http_con import connexion
import json

app = Flask(__name__)
con = connexion()
print(f"Will run on {con.connexion_string()}")


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/metadata")
def get_data():
    f = open("server/data.json")
    config = json.load(f)
    f.close()
    return config["metadata"]


@app.route("/logs", methods=["GET", "POST"])
def logs():
    f = open("server/data.json", "r")
    data = json.load(f)
    f.close()
    if request.method == "GET":
        return data["logs"]
    else:
        new_log = request.form.get("log")
        if new_log:
            data["logs"].append(new_log)
            f = open("server/data.json", "w")
            json.dump(data, f)
            f.close()
        return "ok"


if __name__ == "__main__":
    app.run(host="localhost", port=con.PORT, debug=True)
