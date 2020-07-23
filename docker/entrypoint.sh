#!$SHELL
set -e

python manage.py migrate
python manage.py collectstatic

if [ "$STAGE" = 'dev' ] 
then
    echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'pass')" | python manage.py shell
fi

envsubst < nginx.conf > /etc/nginx/nginx.conf
nginx
gunicorn SnippetManager.wsgi