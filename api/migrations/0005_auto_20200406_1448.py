# Generated by Django 3.0.5 on 2020-04-06 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200405_2317'),
    ]

    operations = [
        migrations.AddField(
            model_name='anonymousmetrics',
            name='heart_rate_diff',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='anonymousmetrics',
            name='saturation_diff',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]