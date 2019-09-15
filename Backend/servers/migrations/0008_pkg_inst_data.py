# Generated by Django 2.2.5 on 2019-09-15 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0004_projects'),
        ('servers', '0007_list_parent_server'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pkg_inst_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PackageId', models.IntegerField()),
                ('PackageName', models.CharField(default='', max_length=250)),
                ('PackageStatus', models.CharField(default='', max_length=250)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('server', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servers.list')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='signup.user')),
            ],
        ),
    ]
