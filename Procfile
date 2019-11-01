release: python manage.py migrate --run-syncdb
release: python manage.py migrate --fake pokebattle
release: python manage.py migrate
web: gunicorn pokemon.wsgi --log-file -
