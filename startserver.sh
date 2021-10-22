export SECRET_KEY='django-insecure-#8a_&89dp)4&!yt3i)vf_#pq2fp^z7tz$=42i(pb((38c599t5'
python manage.py migrate
cat <<EOF | python manage.py shell
from django.contrib.auth import get_user_model
User = get_user_model()
User.objects.filter(username='admin').exists() or \
    User.objects.create_superuser('admin', 'admin@example.com', 'pass')
EOF
python manage.py runserver 0.0.0.0:8000
