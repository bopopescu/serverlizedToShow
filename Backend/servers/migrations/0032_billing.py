# Generated by Django 2.2.5 on 2019-10-17 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0008_transation_date'),
        ('servers', '0031_notifications_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='billing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=75)),
                ('status', models.BooleanField(default=True)),
                ('monthly_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('server', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servers.list')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='signup.user')),
            ],
        ),
    ]
