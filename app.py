import os
from flask import Flask, render_template, redirect, url_for, request
from dotenv import load_dotenv
from config import Config
from models import db, Visitor

load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    @app.route("/")
    def home():
        return render_template("index.html")

    @app.route("/register")
    def register():
        return render_template("visitor_form.html")

    @app.route("/save", methods=["POST"])
    def save_visitor():
        name = request.form.get("name")
        phone = request.form.get("phone")
        purpose = request.form.get("purpose")

        if not name or not phone or not purpose:
            return redirect(url_for("register"))

        visitor = Visitor(name=name, phone=phone, purpose=purpose)
        db.session.add(visitor)
        db.session.commit()

        return redirect(url_for("visitor_list"))

    @app.route("/visitors")
    def visitor_list():
        visitors = Visitor.query.order_by(Visitor.created_at.desc()).all()
        return render_template("visitor_list.html", visitors=visitors)

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")