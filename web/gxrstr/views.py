from flask import render_template
from gxrstr import app


@app.route("/")
@app.route("/index.html")
def main_root():
    return render_template("index.html")
