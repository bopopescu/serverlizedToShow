# Generated by Django 2.2.5 on 2019-10-13 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0028_server_stats'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='server_stats',
            name='user',
        ),
    ]
