# Generated by Django 4.0 on 2022-01-04 22:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='project_image',
            new_name='image',
        ),
    ]
