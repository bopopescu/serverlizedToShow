# Generated by Django 2.2.5 on 2019-09-10 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0006_list_superuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='parent_server',
            field=models.CharField(default='', max_length=250),
        ),
    ]
