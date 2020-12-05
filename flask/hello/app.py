from flask import Flask, Blueprint, render_template


def url_join(*path):
    return ("/" + "/".join(path)).replace("//", "/")


def create_app(base_url='/hello'):
    from .api import api

    app = Flask(__name__, static_url_path=url_join(base_url, "static"))

    root = Blueprint("hello", __name__)

    @root.route('/')
    def index():
        return render_template("index.html")

    app.add_url_rule(url_join(base_url), 'index', index)
    app.register_blueprint(root, url_prefix=url_join(base_url))
    app.register_blueprint(api, url_prefix=url_join(base_url, "api"))
    return app
