# Generated by Django 4.2.14 on 2024-08-04 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_election_creation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='candiates',
            name='number_of_votes',
            field=models.IntegerField(default=0),
        ),
    ]
