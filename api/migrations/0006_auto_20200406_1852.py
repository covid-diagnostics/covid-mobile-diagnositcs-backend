# Generated by Django 3.0.5 on 2020-04-06 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20200406_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anonymousmetrics',
            name='measurement_method',
            field=models.TextField(choices=[('phone on the measuring hand', 'phone on the measuring hand'), ('phone on the other hand', 'phone on the other hand'), ('phone on the table', 'phone on the table')]),
        ),
    ]