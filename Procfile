web: gunicorn sicwebapp.wsgi --log-file -
release: python sicwebapp/manage.py makemigrations --noinput
release: python sicwebapp/manage.py migrate --noinput
