# Generated by Django 2.2.1 on 2019-06-01 21:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20190601_2338'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Stage',
            new_name='Stages',
        ),
        migrations.RenameModel(
            old_name='User',
            new_name='Users',
        ),
        migrations.RenameModel(
            old_name='UserStage',
            new_name='UserStages',
        ),
    ]