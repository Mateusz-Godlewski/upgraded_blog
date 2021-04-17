from flask import Flask, render_template, request
import requests


app = Flask(__name__)


@app.route("/")
@app.route("/index.html")
def home():
    response = requests.get(url="https://api.npoint.io/0067e63917ca7a5034d9").json()
    return render_template("index.html", response=response)


# @app.route("/success.html", methods=["POST"])
# def success():
#     return render_template("success.html")


@app.route("/contact.html", methods=["GET", "POST"])
def contact_page():
    if request.method == "POST":
        heading = "Successfully sent your message!"
        username = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        print(f"{username}, {email}, {phone}, {message}")
        return render_template("contact.html", username=username, email=email, phone=phone, message=message, heading=heading)
    else:
        heading = "Contact Me"
        return render_template("contact.html", heading=heading)


@app.route("/post.html/<num>")
def post(num):
    response = requests.get(url="https://api.npoint.io/0067e63917ca7a5034d9").json()
    blog_post = response[int(num) - 1]
    return render_template("post.html", num=num, response=blog_post)


@app.route("/<name>")
def page(name):
    return render_template(name)


if __name__ == "__main__":
    app.run(debug=True)