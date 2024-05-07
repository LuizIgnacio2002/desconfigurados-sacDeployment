set -o errexit
# poetry install
pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
if [ "$CREATE_SUPERUSER" = "true" ]; then
    export DJANGO_SUPERUSER_USERNAME="admin"
    export DJANGO_SUPERUSER_EMAIL="admin@example.com"
    export DJANGO_SUPERUSER_PASSWORD="admin"
    export DJANGO_SUPERUSER_NOMBRES="admin"

    echo "from myapp.models import User; User.objects.create_superuser(nombres='$DJANGO_SUPERUSER_NOMBRES', username='$DJANGO_SUPERUSER_USERNAME', email='$DJANGO_SUPERUSER_EMAIL', password='$DJANGO_SUPERUSER_PASSWORD')" | python manage.py shell
fi
