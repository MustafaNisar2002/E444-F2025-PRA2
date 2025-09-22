# app.py
from datetime import datetime
from flask import Flask, render_template, session, redirect, url_for, flash
from flask_moment import Moment
from forms import NameEmailForm

app = Flask(__name__)
# IMPORTANT: change this in production; keeping it here for the PRA demo.
app.config["SECRET_KEY"] = "change-this-in-production"

moment = Moment(app)

@app.route("/", methods=["GET", "POST"])
def index():
    form = NameEmailForm()
    if form.validate_on_submit():
        old_name = session.get("name")
        old_email = session.get("email")

        session["name"] = form.name.data.strip()
        session["email"] = form.email.data.strip()

        if (old_name and old_name != session["name"]) or (old_email and old_email != session["email"]):
            flash("Looks like you updated your info!")

        # Post/Redirect/GET to avoid duplicate submissions on refresh
        return redirect(url_for("index"))

    return render_template(
        "index.html",
        form=form,
        name=session.get("name"),
        email=session.get("email"),
        current_time=datetime.utcnow(),
    )


if __name__ == "__main__":
    app.run(debug=True)
