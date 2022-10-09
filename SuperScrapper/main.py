from flask import Flask, render_template

app = Flask("SuperScrapper")

@app.route("/")
def home():
    return render_template("potato.html")

@app.route("/report")
def report():
    return "this is the report"

app.run(host = "0.0.0.0")
