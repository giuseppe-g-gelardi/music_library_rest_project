# Generated by Django 3.2.6 on 2021-08-09 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_alter_song_likes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='likes',
            new_name='like',
        ),
    ]
