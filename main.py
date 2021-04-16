from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route("/")
@app.route("/index.html")
def home():
    response = requests.get(url="https://api.npoint.io/0067e63917ca7a5034d9").json()
    return render_template("index.html", response=response)


@app.route("/<name>")
def page(name):
    return render_template(name)


@app.route("/post.html/<num>")
def post(num):
    response = requests.get(url="https://api.npoint.io/0067e63917ca7a5034d9").json()
    # CANT GET INTO THE POST, SAYS ITS A TYPE ERROR, PROBLEM WITH SLICING A JSON DICT
    blog_post = response[num]
    return render_template("post.html", num=num, response=blog_post)


if __name__ == "__main__":
    app.run(debug=True)