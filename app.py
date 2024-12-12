from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "HI from Flask !!"


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=port)
