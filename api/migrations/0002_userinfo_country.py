# Generated by Django 3.0.4 on 2020-05-04 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='country',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
    ]
