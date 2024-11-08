
from django.db import migrations
from django.contrib.auth.models import User

def create_initial_users(apps, schema_editor):
    User = apps.get_model('auth', 'User')

    # Create a superuser to testing purposes
    User.objects.create_superuser('admin', 'admin@example.com', 'admin')

    # create 2 staff users
    User.objects.create_user(
        'staff1', 'staff1@example.com', 'staff1', is_staff=True
    )
    User.objects.create_user(
        'staff2', 'staff2@example.com', 'staff2', is_staff=True
    )

    # Crear usuarios normales
    for i in range(3, 11):
        User.objects.create_user(
            f'user{i}', f'user{i}@example.com', 'userpassword'
        )


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_initial_users),
    ]