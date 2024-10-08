# Generated by Django 4.2.14 on 2024-08-04 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_apis', '0004_delete_candiates_delete_create_elections'),
    ]

    operations = [
        migrations.CreateModel(
            name='candiates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=12345678)),
                ('postion', models.CharField(max_length=1234356478)),
            ],
        ),
        migrations.CreateModel(
            name='create_elections',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=12345678)),
                ('number_of_candidates', models.IntegerField(default=0)),
                ('organizer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login_apis.users')),
            ],
        ),
    ]
