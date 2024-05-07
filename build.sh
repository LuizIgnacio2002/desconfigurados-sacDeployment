set -o errexit
# poetry install
pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
if [ "$CREATE_SUPERUSER" = "true" ]; then
    echo "Creating superuser..."
    echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', getenv('DJANGO_SUPERUSER_EMAIL', 'admin@example.com'), getenv('DJANGO_SUPERUSER_PASSWORD', '123'))" | python manage.py shell
fi
