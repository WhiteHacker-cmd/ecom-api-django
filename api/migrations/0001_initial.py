from django.db import migrations
from api.user.models import CustomUser


class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        user = CustomUser(name="amal",
                          email="amal@ak.dev",
                          is_staff=True,
                          is_superuser=True,
                          phone="80808080",
                          gender="Male",
                          is_active=True
                          )
        user.set_password("1234")
        user.save()

    dependencies = [

    ]

    operations = [
        migrations.RunPython(seed_data),
    ]
