# Generated by Django 3.2.3 on 2021-05-19 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0002_rename_opus_opuses'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Opuses',
            new_name='Opus',
        ),
    ]