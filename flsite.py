from flask import Flask, render_template, url_for, request, flash, session, redirect, abort

app = Flask(__name__)
app.config["SECRET_KEY"] = "gfrge43534hb34g344gh3g3h435g"

menu = [{"name": "Install", "url": "install-flask"},
        {"name": "First app", "url": "first-app"},
        {"name": "Call back", "url": "contact"}]

@app.route("/index")
@app.route("/")
def index():
    print(url_for("index"))
    return render_template("index.html", menu=menu)

@app.route("/about")
def about():
    print(url_for("about"))
    return render_template("about.html", title="About site", menu=menu)

@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        if len(request.form["username"]) > 2:
            flash("Massage sent", category="success")
        else:
            flash("Error of message", category="error")

    return render_template("contact.html", title="Contact us", menu=menu)

@app.errorhandler(404)
def page_not_fount(error):
    return render_template("page404.html", title="Page not found", menu=menu), 404

@app.route("/login", methods=["POST", "GET"])
def login():
    print("++++++", session)
    if "userLogged" in session:
        return redirect(url_for("profile", username=session["userLogged"]))
    elif request.method == "POST" and request.form["username"] == "Misha" and request.form['psw'] == "123":
        session["userLogged"] = request.form['username']
        return redirect(url_for("profile", username=session["userLogged"]))
    return render_template("login.html", title="Autorization", menu=menu)

@app.route("/profile/<username>")
def profile(username):
    print("-----", username)
    if "userLogged" not in session or session["userLogged"] != username:
        abort(401)
    return f"Profile user: {username}"


if  __name__ == "__main__":
    app.run(debug=True) 