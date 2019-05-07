release: 
  python manage.py migrate --noinput &&
  python manage.py makemigrations --noinput    

web:
  gunicorn backend.wsgi --log-file -
