# Generated by Django 2.2.5 on 2019-10-16 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0005_auto_20191016_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transation',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
        ),
    ]