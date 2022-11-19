from flask import Flask
from http_con import connexion

app = Flask(__name__)
con = connexion()
print(f"Will run on {con.connexion_string()}")


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run(host="localhost", port=con.PORT, debug=True)
