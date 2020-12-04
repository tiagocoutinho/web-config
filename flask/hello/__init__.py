from flask import Flask, render_template


def patch_route(app, prefix=''):
    if prefix:
        route = app.route
        app.route = lambda rule, **opts: route(prefix + rule, **opts)


def create_app(url_prefix='/bla'):
    app = Flask(__name__)
    patch_route(app, url_prefix)

    @app.route('/')
    def index():
        return render_template("index.html")

    from .api import api
    app.register_blueprint(api)
    return app

