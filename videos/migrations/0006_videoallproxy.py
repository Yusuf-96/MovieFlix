# Generated by Django 3.2.2 on 2021-05-09 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0005_video_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='videoAllProxy',
            fields=[
            ],
            options={
                'verbose_name': 'All video',
                'verbose_name_plural': 'All Videos',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('videos.video',),
        ),
    ]
