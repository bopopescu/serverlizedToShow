# Generated by Django 2.2.5 on 2019-09-09 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0005_list_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='superuser',
            field=models.CharField(default='', max_length=55),
        ),
    ]
