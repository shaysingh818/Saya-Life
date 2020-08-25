# Generated by Django 3.0.8 on 2020-08-13 21:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('billing', '0002_remove_profile_hcf_usage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='to_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
