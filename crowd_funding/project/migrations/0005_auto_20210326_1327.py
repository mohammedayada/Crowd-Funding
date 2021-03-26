# Generated by Django 3.1.7 on 2021-03-26 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_auto_20210324_2058'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='avg_rate',
            new_name='sum_rate',
        ),
        migrations.AddField(
            model_name='project',
            name='count_rated_user',
            field=models.IntegerField(default=0),
        ),
    ]
