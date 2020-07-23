---
title: URL Shortener
author: Markus
---

# URL Shortener

Small Django-App which allows you to shorten URLS. The default credentials for the dev instance are:

- `username: admin`
- `password: pass`

# Docker

```bash
docker run -e DJANGO_SECRET_KEY="secret" -e HOST_HEADER1="127.0.0.1" -e HOST_HEADER2="127.0.0.1" -e STAGE="dev" -p 80:80 url
```

Login at `http://127.0.0.1:80/admin/login/`

# Run the App outside a Container

```bash
export STAGE="dev"
export DJANGO_SECRET_KEY="secret"
python app/manage.py makemigrations
python app/manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'pass')" | python app/manage.py shell
python app/manage.py runserver
```
Login at `http://127.0.0.1:8000/admin/login/`