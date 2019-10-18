# Generated by Django 2.2.5 on 2019-10-17 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0008_transation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transation',
            name='amount',
            field=models.DecimalField(decimal_places=10, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='money',
            field=models.DecimalField(decimal_places=10, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='monthly_charges',
            field=models.DecimalField(decimal_places=10, default=0.0, max_digits=10),
        ),
    ]