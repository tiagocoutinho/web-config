from gevent.monkey import patch_all
patch_all()
from gevent.pywsgi import WSGIServer
import click

from .app import create_app


@click.command("run", short_help="Run gevent based WSGI server.")
@click.option("--host", "-h", default="127.0.0.1", help="The interface to bind to.")
@click.option("--port", "-p", default=5000, help="The port to bind to.")
@click.option("--base-url", "-b", default=None)
def run(host, port, base_url):
    """
    $ python -m hello.gevent -h 0 -p 5000 -b /hello

    You can also use ENV variables:

    $ HELLO_BASE_URL=/hello python -m hello.gevent -h 0 -p 5000

    """
    app = create_app(base_url=base_url)
    http_server = WSGIServer((host, port), app)
    http_server.serve_forever()


if __name__ == '__main__':
    run(auto_envvar_prefix='HELLO')
