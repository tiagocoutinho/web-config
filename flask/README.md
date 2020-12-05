## Launching

After preparing with one of the options below, point your web browser to
http://0:5000/hello.

REST API in http://0:5000/hello/api (ex: http://0:5000/hello/api/hello).

### Basic development run

```
FLASK_APP=hello.app flask run -h 0
```

* `FLASK_APP=hello.wsgi` should also work
* custom URL prefix: `FLASK_APP=hello.app.create_app('/world')`

### Standalone WSGI containers

#### *uWSGI*

(see also [uwsgi.ini](uwsgi.ini))

```
uwsgi --http 0:5000 --module hello.wsgi:app --threads=10
```

If you want gevent please patch early:
```
uwsgi --http 0:5000 --module hello.wsgi:app --gevent-early-monkey-patch --gevent=100
```

#### *gunicorn*

```
gunicorn --bind 0:5000 hello.wsgi:app --worker-class=gevent
```

### Run in nginx

Prepare directories for first run:

```
mkdir -p var/log/nginx
mkdir -p var/run/nginx
mkdir -p var/tmp/nginx
```

#### *uWSGI*

(see also [uwsgi-nginx.ini](uwsgi-nginx.ini) & [nginx-uwsgi.conf](nginx-uwsgi.conf))

```
uwsgi --ini ./uwsgi-nginx.ini
```

```
nginx -p . -c nginx-uwsgi.conf
```

#### *gunicorn*

(see also [gunicorn.conf.py](gunicorn.conf.py) & [nginx-gunicorn.conf](nginx-gunicorn.conf))

```
gunicorn -c ./gunicorn.conf.py  "hello.app:create_app('/gunicorn')"
```

```
nginx -p . -c nginx-gunicorn.conf
```
