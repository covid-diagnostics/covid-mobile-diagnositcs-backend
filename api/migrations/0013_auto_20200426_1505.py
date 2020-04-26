# Generated by Django 3.0.5 on 2020-04-26 12:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20200425_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='measurements', to=settings.AUTH_USER_MODEL),
        ),
    ]
