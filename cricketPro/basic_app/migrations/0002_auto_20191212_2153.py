# Generated by Django 2.2.7 on 2019-12-12 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='role',
        ),
        migrations.AlterField(
            model_name='matchresult',
            name='winner',
            field=models.IntegerField(choices=[(1, 'Host Team'), (2, 'Opponent Team'), (3, 'Not Yet Played')], default=3),
        ),
    ]
