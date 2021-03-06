# Generated by Django 3.1.7 on 2021-03-24 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_project_report_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='project_imgs',
            name='img',
            field=models.ImageField(upload_to='projects_pictures/'),
        ),
    ]
