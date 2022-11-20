from flask import Flask, request
import json

app = Flask(__name__)


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


@app.route("/logs/<int:id>", methods=["DELETE", "PATCH"])
def admin(id):
    f = open("server/data.json", "r")
    data = json.load(f)
    f.close()
    if request.method == "DELETE":
        try:
            del data["logs"][id]
            f = open("server/data.json", "w")
            json.dump(data, f)
            f.close()
            return "ok"
        except:
            return "error"
    else:
        category = request.form.get("category")
        if category:
            try:
                example = data["logs"][id]
                f = open("server/data.json", "w")
                data["metadata"][category].append(example)
                del data["logs"][id]
                json.dump(data, f)
                f.close()
                return "ok"
            except Exception as err:
                return str(err)


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
