import time
import threading

from flask import Blueprint, Response, redirect, url_for


def source():
    name = threading.current_thread().name
    for i in range(40, 0, -1):
        time.sleep(0.25)
        data = dict(event=i, thread=name)
        yield f"data: {data}\n\n"


api = Blueprint("api", __name__)


@api.route('/')
def index():
    return redirect(url_for('index'))


@api.route('/hello')
def hello_world():
    return dict(hello='world')


@api.route('/stream')
def stream():
    return Response(source(), mimetype="text/event-stream")
