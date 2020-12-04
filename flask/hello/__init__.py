from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template("index.html")

    from .api import api
    app.register_blueprint(api)

    return app

