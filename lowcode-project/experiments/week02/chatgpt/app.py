
import re
from flask import Flask, render_template, request

app = Flask(__name__)


def valid_email(email):
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    return re.fullmatch(pattern, email) is not None


@app.route("/contact", methods=["GET", "POST"])
def contact():
    errors = {}
    name = ""
    email = ""
    message = ""

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()

        if not name:
            errors["name"] = "Please enter your name."

        if not valid_email(email):
            errors["email"] = "Please enter a valid email address."

        if not message:
            errors["message"] = "Please enter a message."

        if not errors:
            return render_template("confirmation.html")

    return render_template(
        "contact.html",
        errors=errors,
        name=name,
        email=email,
        message=message
    )


if __name__ == "__main__":
    app.run()
