from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello")

@app.route("/random")
def get_random():
    number = random.randint(1, 100)
    return jsonify({"random_number": number})