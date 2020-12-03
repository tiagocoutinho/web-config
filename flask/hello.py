import time
import threading

from flask import Flask, Response, render_template


app = Flask(__name__)


def source():
    name = threading.current_thread().name
    for i in range(100):
        time.sleep(0.05)
        data = dict(event=i, thread=name)
        yield f"data: {data}\n\n"


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/hello/')
def hello_world():
    return 'Hello, World!'


@app.route('/stream/')
def stream():
    return Response(source(), mimetype="text/event-stream")
