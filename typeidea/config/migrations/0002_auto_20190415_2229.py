# Generated by Django 2.2 on 2019-04-15 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='link',
            old_name='herf',
            new_name='href',
        ),
    ]
