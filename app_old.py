from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta

# creating main Flask object
app = Flask(__name__)
app.secret_key = "3%316373$fcvhd4345c$gf/f"
app.permanent_session_lifetime = timedelta(minutes=1)

# route for index page
@app.route('/') # @ <- this thing is called 'decorator'
def index():
    return render_template("index.html") # use index.html file to show page

# route for page with url '/' + some string, which is passed to funcion
# @app.route('/<name>')
# def user(name):
#     return render_template("user.html", content=name)

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

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return render_template("user.html", user=user)
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
    
    return redirect(url_for("login"))

if __name__ == '__main__':
    app.run(debug=True)
