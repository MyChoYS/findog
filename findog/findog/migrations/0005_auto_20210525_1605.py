# Generated by Django 3.1.5 on 2021-05-25 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('findog', '0004_auto_20210525_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='missingdog',
            name='delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mydog',
            name='delete',
            field=models.BooleanField(default=False),
        ),
    ]
