from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
import sqlalchemy

app = Flask(__name__)
app.secret_key = "3%316373$fcvhd4345c$gf/f"
app.permanent_session_lifetime = timedelta(minutes=1)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["name"]
        session["user"] = user
        flash("Lognięte", "info")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Już przecież zalogowany jesteś typie", "info")
            return redirect(url_for("user"))
        
        return render_template("login.html")

@app.route("/user", methods=['GET', 'POST'])
def user():
    email = None
    if "user" in session:
        user = session["user"]
        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            flash("Email zapamiętany ziom", "info")
        else:
            if "email" in session:
                email = session["email"]
        return render_template("user.html", email=email)
    else:
        flash("A może się zaloguj najpierw?", "info")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    if "user" in session:
        user = session["user"]
        flash("Wylogowaned", "info")
        flash("Wypad powiedziałem!", "info")
    else:
        flash("Z czego niby chcesz się wylogować?", "info")

    session.pop("user", None)
    session.pop("email", None)
    
    return redirect(url_for("login"))

if __name__ == '__main__':
    app.run(debug=True)
