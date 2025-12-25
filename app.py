from flask import Flask, render_template, request, redirect, url_for, session
import json, os
import config

app = Flask(__name__)
app.secret_key = config.SECRET_KEY

DATA_FILE = "data/submissions.json"

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    form_data = {
        "name": request.form["name"],
        "email": request.form["email"],
        "phone": request.form["phone"],
        "message": request.form["message"]
    }

    with open(DATA_FILE, "r+") as f:
        data = json.load(f)
        data.append(form_data)
        f.seek(0)
        json.dump(data, f, indent=4)

    return redirect(url_for("success"))

@app.route("/success")
def success():
    return render_template("success.html")

# 🔐 Login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if (request.form["username"] == config.ADMIN_USERNAME and
                request.form["password"] == config.ADMIN_PASSWORD):
            session["admin"] = True
            return redirect(url_for("admin"))
    return render_template("login.html")

# 🔒 Protected Admin
@app.route("/admin")
def admin():
    if not session.get("admin"):
        return redirect(url_for("login"))

    with open(DATA_FILE) as f:
        data = json.load(f)

    return render_template("admin.html", submissions=data, count=len(data))

@app.route("/logout")
def logout():
    session.pop("admin", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
