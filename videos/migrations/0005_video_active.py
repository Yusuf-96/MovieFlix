# Generated by Django 3.2.2 on 2021-05-09 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0004_alter_videoproxy_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
