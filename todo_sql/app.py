from flask import Flask


app = Flask(__name__)
app.config["SECRET_KEY"] = "kotwlodek"


import views


if __name__ == "__main__":
    app.run(debug=True)



