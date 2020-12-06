## Launching

After preparing with one of the options below, point your web browser to
http://localhost:5000.

REST API in http://localhost:5000/hello/api (ex: http://localhost:5000/api/hello).

### Basic development run

```
FLASK_APP=hello.app flask run -h 0
```

* `FLASK_APP=hello.wsgi` should also work
* custom URL prefix:
  1. `FLASK_APP=hello.app.create_app('/hello')` or
  2. add env `HELLO_BASE_URL=/hello`

### Standalone WSGI containers

#### *gevent*

```
python -m hello.gevent -h 0 -p 5000
```

#### *gunicorn*

```
gunicorn -b 0:5000 --worker-class=gevent hello.wsgi:app
```

*Different base URL:*

```
gunicorn -b 0:5000 --worker-class=gevent -e HELLO_BASE_URL=/hello hello.wsgi:app
```

...or, in a config file add:

```python
raw_env = ["HELLO_BASE_URL=/hello"]
```

#### *uWSGI*

(see also [uwsgi.ini](uwsgi.ini))

```
uwsgi --http 0:5000 --module hello.wsgi:app --threads=10
```

If you want gevent please patch early:

```
uwsgi --http 0:5000 --module hello.wsgi:app --gevent-early-monkey-patch --gevent=100
```

### Run in nginx

Prepare directories for first run:

```
mkdir -p var/log/nginx
mkdir -p var/run/nginx
mkdir -p var/tmp/nginx
```

#### *gevent*

```
python -m hello.gevent -h 0 -p 5000 -b /gevent
```

```
nginx -p . -c nginx-gevent.conf
```

#### *gunicorn*

(see also [gunicorn.conf.py](gunicorn.conf.py) & [nginx-gunicorn.conf](nginx-gunicorn.conf))

```
gunicorn -c ./gunicorn.conf.py hello.wsgi:app
```

```
nginx -p . -c nginx-gunicorn.conf
```

#### *uWSGI*

**Important**: I did not manage to get SSE working with uwsgi yet!

(see also [uwsgi-nginx.ini](uwsgi-nginx.ini) & [nginx-uwsgi.conf](nginx-uwsgi.conf))

```
uwsgi --ini ./uwsgi-nginx.ini
```

```
nginx -p . -c nginx-uwsgi.conf
```
