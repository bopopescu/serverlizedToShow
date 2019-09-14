# Generated by Django 2.2.5 on 2019-09-12 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lamp', '0002_mysql_database_mysql_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mysql_user',
            name='domain_name',
        ),
        migrations.AddField(
            model_name='mysql_user',
            name='remote',
            field=models.BooleanField(default=False),
        ),
    ]
