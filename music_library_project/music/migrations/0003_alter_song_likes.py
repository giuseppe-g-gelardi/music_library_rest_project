# Generated by Django 3.2.6 on 2021-08-09 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_song_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='likes',
            field=models.IntegerField(),
        ),
    ]
