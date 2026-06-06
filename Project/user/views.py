import flask
import flask_login
import random
import werkzeug.security as security

from Project.db import DATA_BASE
from .models import User
from flask_mail import Message
from Project.settings import mail


def render_login():
    errors = {}

    if flask.request.method == "GET":
        next_url = flask.request.args.get("next")

        if next_url:
            flask.session["next_url"] = next_url

        return flask.redirect("/?modal=login")

    email = flask.request.form.get("email", "").strip()
    password = flask.request.form.get("password", "")

    if not email:
        errors["email"] = "Введіть email"

    if not password:
        errors["password"] = "Введіть пароль"

    user = User.query.filter_by(email=email).first()

    if not errors:
        if user is None:
            errors["email"] = "Користувача з таким email не знайдено"

        elif not security.check_password_hash(user.password, password):
            errors["password"] = "Невірний пароль"

        else:
            flask_login.login_user(user)

            redirect_url = flask.session.pop("next_url", "/")

            return flask.jsonify({
                "success": True,
                "redirect": redirect_url
            })

    html = flask.render_template("login.html", errors=errors)

    return flask.jsonify({
        "success": False,
        "html": html,
        "modal": "login"
    })


def render_register():
    errors = {}

    if flask.request.method == "GET":
        html = flask.render_template("register.html", errors={})

        return flask.jsonify({
            "success": False,
            "html": html
        })

    name = flask.request.form.get("first_name", "").strip()
    email = flask.request.form.get("email", "").strip()
    password = flask.request.form.get("password", "")
    confirm_password = flask.request.form.get("confirm_password", "")

    if len(name) < 3:
        errors["first_name"] = "Ім'я має містити мінімум 3 символи"

    if not email:
        errors["email"] = "Введіть email"

    if len(password) < 8:
        errors["password"] = "Пароль має містити мінімум 8 символів"

    if password != confirm_password:
        errors["confirm_password"] = "Паролі не співпадають"

    user_email = User.query.filter_by(email=email).first()

    if user_email is not None:
        errors["email"] = "Користувач з таким email вже існує"

    if errors:
        html = flask.render_template("register.html", errors=errors)

        return flask.jsonify({
            "success": False,
            "html": html,
            "modal": "register"
        })

    code = ""

    for _ in range(6):
        code += str(random.randint(0, 9))

    msg = Message(
        "Email confirm",
        recipients=[email],
        sender="lenafedchenko07@gmail.com",
        body=code
    )

    msg.html = f"""
        <html lang="uk">
        <body style="margin: 0; padding: 0; background-color: #f4f4f4">
            <div style="max-width: 500px; margin:40px auto; background-color: #ffffff;
            padding: 24px; border-radius: 6px; text-align: center">
                <h2 style="color: black">Підтвердження пошти</h2>
                <p style="font-size: 16px; color:grey">Ваш код підтвердження:</p>
                <div style="font-size: 28px; font-weight: bold; color: black;
                margin: 20px; letter-spacing: 4px">
                    {code}
                </div>
                <p style="font-size: 13px; color: #888">
                    Якщо ви не реєструвалися, проігноруйте цей лист
                </p>
            </div>
        </body>
        </html>
    """

    mail.send(msg)

    flask.session["verify_code"] = code
    flask.session["name"] = name
    flask.session["email"] = email
    flask.session["password"] = password

    html = flask.render_template("verify_code.html", errors={})

    return flask.jsonify({
        "success": False,
        "html": html,
        "modal": "verify"
    })


def render_verify():
    errors = {}

    if flask.request.method == "GET":
        html = flask.render_template("verify_code.html", errors={})

        return flask.jsonify({
            "success": False,
            "html": html
        })

    verify_code = ""

    for value in flask.request.form.values():
        verify_code += value.strip()

    if len(verify_code) != 6:
        errors["verify_code"] = "Код має містити 6 цифр"

    elif flask.session.get("verify_code") != verify_code:
        errors["verify_code"] = "Невірний код підтвердження"

    else:
        password = flask.session.get("password")

        hashed_password = security.generate_password_hash(
            password,
            salt_length=10
        )

        user = User(
            first_name=flask.session.get("name"),
            email=flask.session.get("email"),
            password=hashed_password
        )

        DATA_BASE.session.add(user)
        DATA_BASE.session.commit()

        flask_login.login_user(user)

        flask.session.pop("verify_code", None)
        flask.session.pop("name", None)
        flask.session.pop("email", None)
        flask.session.pop("password", None)

        return flask.jsonify({
            "success": True,
            "redirect": "/"
        })

    html = flask.render_template("verify_code.html", errors=errors)

    return flask.jsonify({
        "success": False,
        "html": html,
        "modal": "verify"
    })


def logout():
    flask.session.clear()
    flask_login.logout_user()

    return flask.redirect("/")