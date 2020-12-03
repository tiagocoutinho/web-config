## Launching

### Basic development run

```
FLASK_APP=hello flask run -p 5000
```

### Run in nginx

```
mkdir -p var/log/nginx
mkdir -p var/run/nginx
mkdir -p var/tmp/nginx
```

```
nginx -p .
```
