# Generated by Django 2.2.5 on 2019-09-15 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0008_pkg_inst_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='pkg_inst_data',
            name='ViewPKGOption',
            field=models.BooleanField(default=True),
        ),
    ]
